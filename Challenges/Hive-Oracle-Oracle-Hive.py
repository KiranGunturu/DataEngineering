##Oracle to Hive

import sys
from pyspark import SparkContext, SQLContext, SparkConf, HiveContext
import yaml
import json
from subprocess import call
from pyspark.sql import SparkSession
import cx_Oracle
import sys
from pyspark.sql.window import Window
import pyspark.sql.functions as func
from pyspark.sql.functions import *

query = """
(
select
  col1,
  col2,
  col3,
  ...
from table_name
) v_table_name
"""

df_oracle = spark.read
    .format("jdbc")
    .option("url", "jdbc:oracle:thin:@hostname:port:SID")
    .option("user",userName)
    .option("password",passWord)
    .option("driver", "oracle.jdbc.driver.OracleDriver")
    .option("dbtable", query)
    .load()

df_oracle.repartition(10).write.format("orc").mode("overwrite").saveAsTable(outputTable)



## Hive to Oracle

import sys
from pyspark import SparkContext, SQLContext, SparkConf, HiveContext
import yaml
import json
from subprocess import call
from pyspark.sql import SparkSession
import cx_Oracle
import sys
from pyspark.sql.window import Window
import pyspark.sql.functions as func
from pyspark.sql.functions import *


spark = SparkSession \
        .builder \
        .appName("Hive to Oracle Load") \
        .enableHiveSupport() \
        .getOrCreate()


spark.sparkContext.setLogLevel("ERROR") 

def write_oracle_db(hostname,db_user,db_pswd,db_schema,oracleTable,db_mode,source_table1):
        
        try:
                        stmt="select col1, \
                              col2, \
                              col3, \
                              col4, \
                              col5 from {0}".format(source_table1)
                        print(stmt)
                        connection = cx_Oracle.connect(user=db_user, password=db_pswd, dsn=hostname,encoding="UTF-8")
                        cur = connection.cursor()
                        sql = "select case when max(PK) is null then 0 else max(PK) end as ID from " + db_schema + "." + oracleTable
                        cur.execute(sql)
                        print(sql)
                        MaxOracleValue = cur.fetchone()
                        print(MaxOracleValue)
                        MaxOracleValue = int(''.join(map(str, MaxOracleValue)))
                        print(MaxOracleValue)                      
                        df = spark.sql(stmt).withColumn("cdate", current_date()).withColumn('ctime',current_timestamp())
                        windowSpec = Window.orderBy(df['somecolumn'])
                        df1 = df.withColumn('PK', row_number().over(windowSpec) + MaxOracleValue)
                        print(df1.show())
                        df1.write.format('jdbc').options(url='jdbc:oracle:thin:@' + hostname,
                                                         driver='oracle.jdbc.driver.OracleDriver',
                                                         dbtable=db_schema + "." + oracleTable1, user=db_user,
                                                         password=db_pswd).mode(db_mode).save()

                        print("hostname-",hostname)
                        print("db_schema-",db_schema)
                        print("oracleTable-",oracleTable)
                        print("db_user",db_user)
                        #print("db_pwd",db_pswd)
                        print("db_mode",db_mode)

                        print (self.hostname)
                        
        except Exception as e:
                        print("Exception in data  writing to oracle table)
                        print(str(e))
                        raise sys.exit(1)
                        
                        
    source_table1="hivedb.customer"
    oracleTable="oracledb.customer"
    oracleTable=oracleTable1
    awrite_oracle_db(hostname,db_user,db_pswd,db_schema,oracleTable,db_mode,source_table1)