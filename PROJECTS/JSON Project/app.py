# sys is used for passing and accessing parameters
# os is used to access environment variables
import sys
import os
from pyspark.sql import SparkSession
from util import get_spark_session
from read import read_files
from process import transform
from write import write_to_files

print(type(sys.argv))
print(sys.argv[0])
print(sys.argv[1])
print('Hello World')

print(type(os.environ))
print(os.environ.get('FOO'))
print(f'Hello world from {os.environ.get("FOO")}')


def main():
    env = os.environ.get('ENVIRON')
    src_dir = os.environ.get('SRC_DIR')
    src_file_pattern = f'{os.environ.get("SRC_FILE_PATTERN")}-x'
    src_file_format = os.environ.get('SRC_FILE_FORMAT')
    tgt_dir = os.environ.get('TGT_DIR')
    tgt_file_format = os.environ.get('TGT_FILE_FORMAT')
    spark = get_spark_session(env, 'Github Activity')
    df = read_files(spark, src_dir, src_file_pattern, src_file_format)
    df_transformed = transform(df)
    df_transformed.prinntSchema()
    df_transformed.select('repo.*','created_at','year','month','day').show()  # //repo is a nested json
    write_to_files(df_transformed, tgt_dir, tgt_file_format) # //json to parquet


if __name__ == "__main__":
    main()
