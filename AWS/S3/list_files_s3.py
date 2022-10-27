def list_s3_files_using_client():
    
    s3_client = boto3.client("s3")
    bucket_name = "testbucket-frompython-2"
    response = s3_client.list_objects_v2(Bucket=bucket_name)
    files = response.get("Contents")
    for file in files:
        print(f"file_name: {file['Key']}, size: {file['Size']}")