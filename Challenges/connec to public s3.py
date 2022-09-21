import requests
import boto3
from botocore.handlers import disable_signing

s3 = boto3.client('s3')
print(s3)
s3=boto3.resource('s3')
s3.meta.client.meta.events.register('choose-signer.s3.*', disable_signing)
bucketname=s3.Bucket('coderbytechallengesandbox')
for i in bucketname.objects.filter(Prefix='__cb__'):
    print(i.key)