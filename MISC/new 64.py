source
=======

CustomerID,Title,FirstName,LastName,CompanyName,EmailAddress,Phone,ZipCode

Destination
===========

CustomerID,Title,FirstName,LastName,CompanyName,EmailAddress,Phone,ZipCode,sk_customer_id, effective_date,expiration_date,current_flag

EOW_DATE = "9999-12-31"
SOURCE_PATH = "/Users/KiranGunturu/PycharmProjects/JupyterNotebooks/data/scd2/customer_data.csv"
DEST_PATH = "/Users/KiranGunturu/PycharmProjects/JupyterNotebooks/data/scd2/output/"
TEMP_PATH = "/Users/KiranGunturu/PycharmProjects/JupyterNotebooks/data/scd2/temp_output/"
KEY_LIST = ["customerid"]
type2_cols = ["CompanyName", "EmailAddress", "Phone", "ZipCode"]
scd2_cols = ["effective_date","expiration_date","current_flag"]
DATE_FORMAT = "yyyy-MM-dd"

from pyspark.sql import SparkSession
from pyspark.sql.functions import * 
from pyspark.sql.window import Window
from os import path, listdir

spark = SparkSession.builder.master("local[1]").appName("scd_type2").getOrCreate()

def column_renamer(df, suffix, append):
    """
    input:
        df: dataframe
        suffix: suffix to be appended to column name
        append: boolean value 
                if true append suffix else remove suffix
    
    output:
        df: df with renamed column
    """
    if append:
        new_column_names = list(map(lambda x: x+suffix, df.columns))
    else:
        new_column_names = list(map(lambda x: x.replace(suffix,""), df.columns))
    return df.toDF(*new_column_names)

def get_hash(df, keys_list):
    """
    input:
        df: dataframe
        key_list: list of columns to be hashed    
    output:
        df: df with hashed column
    """
    columns = [col(column) for column in keys_list]
    if columns:
        return df.withColumn("hash_md5", md5(concat_ws("", *columns)))
    else:
        return df.withColumn("hash_md5", md5(lit(1)))

#During first run will be loaded with all records set to effective_date = current_date() 
#expiration_date = "9999-12-31" and current_flag = True
as there is no previous day data 
sk_customer_id is sarrogate key for dataframe
window_spec  = Window.orderBy("customerid")

df_current = spark.read.options(header=True, delimiter=',',inferSchema='True')\
                .csv(SOURCE_PATH)\
                .withColumn("sk_customer_id",row_number().over(window_spec))\
                .withColumn("effective_date",date_format(current_date(), DATE_FORMAT))\
                .withColumn("expiration_date",date_format(lit(EOW_DATE), DATE_FORMAT))\
                .withColumn("current_flag", lit(True))

#write data to DEST_PATH
df_current.write.mode('overwrite')\
        .option("header",True)\
        .option("delimiter",",")\
        .csv(DEST_PATH)

df_current.show()

# Form next run we need to compare current data with history data
# e.g. comparing today's data with yesterday's data

# Create df_current using SOURCE_PATH
df_current = spark.read.options(header=True, delimiter=',',inferSchema='True')\
                        .csv(SOURCE_PATH)

# Create df_history using DEST_PATH
df_history = spark.read.options(header=True, delimiter=',',inferSchema='True')\
                        .csv(DEST_PATH)\
                        .withColumn("effective_date",to_date("effective_date"))\
                        .withColumn("expiration_date",to_date("expiration_date"))CD-2

df_current.show()
df_history.show()

We need to keep track of the maximum surrogate key in the history table as it will be used to create a surrogate key for newly inserted and updated records.

max_sk = df_history.agg({"sk_customer_id_history": "max"}).collect()[0][0]



