filenames = []
prefix='NSCCV'
bucket='nissan-nna-voq-dev-data-us-east-1//inbound/nhtsa/vin/'

get_filenames(s3):
    result = s3.list_objects_v2(Bucket=bucket, Prefix=prefix)
    for item in result['Contents']:
        files = item['Key']
        print(files)
        filenames.append(files) #optional
    return filenames

get_filenames(bucketfolder)

OR

import requests
import boto3
from botocore.handlers import disable_signing

s3 = boto3.client('s3')
print(s3)
s3=boto3.resource('s3')
bucketname=s3.Bucket('nissan-nna-voq-dev-data-us-east-1//inbound/nhtsa/vin/')
for i in bucketname.objects.filter(Prefix='NSCCV'):
    print(i.key)