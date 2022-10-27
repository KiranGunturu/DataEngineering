# To list files and sizes

    import boto3
    s3_client = boto3.client("s3")
    bucket_name = "testbucket-frompython-2"
    response = s3_client.list_objects_v2(Bucket=bucket_name)
    files = response.get("Contents")
    for file in files:
        print(f"file_name: {file['Key']}, size: {file['Size']}")
        
# to list all buckets names in the AWS account

    import boto3
    s3_client=boto3.client('s3')
    buckets = s3_client.list_buckets()['Buckets']
    bucket_names = [bucket['Name'] for bucket in buckets]
    print(bucket_names)
    
# read content from single s3 object(file/key)

    import boto3
    import os
    os.environ.setdefault('AWS_PROFILE', 'itgithubuser')
    s3_client = boto3.client('s3')
    s3_objects = s3_client.list_objects(
        Bucket='itvflightsdata'
        )
    s3_object_key = s3_objects['Contents'][0]['Key']
    s3_object = s3_client.get_object(
        Bucket='itvflightsdata'
        Key=s3_object_key
        )
    file_contents = s3_object['Body'].read().decode('utf-8')
    file_records = file_contents.splitlines() //this will convert above string to list
    file_records[:3] // to read first 3 elements in the list
    
# read content from multiple s3 object(files/keys)

    import boto3
    import os
    os.environ.setdefault('AWS_PROFILE', 'itgithubuser')
    s3_client = boto3.client('s3')
    s3_objects = s3_client.list_objects(
        Bucket='itvflightsdata',
        MaxKeys=10 //to read 10 files
        )
    
    #s3_objects['Contents']
    s3_object_keys = [s3_object['Key'] for s3_object in s3_objects['Contents']] //extracting all keys info to the list
    #s3_object_keys[:3]
    data = []
    for s3_object_key in s3_object_keys:
        s3_object_elements = s3_client. \
                    get_object(
                        Bucket='itvflightsdata',
                        Key=s3_object_key
                        )['Body'].\
                        read().\
                        decode('utf-8').\
                        splitlines()
        data +=s3_object_elements
    len(data)
    
    # if the file size is very big then we have to read file to multiple lists and then write to targets
    # if the file size is small about approach will work
    # we can use iterate chunks to read big files
    
#list_objects()
    # one of the way to get s3 object metadata from a given bucket is to use list_objects
    #however, list_objects gets metadata only for 1000 objects at max
    #we need to paginate using Marker and iterate untill we get details about all the objects
    
    
# get number of s3 objects using marker

    
    import boto3
    import os
    os.environ.setdefault('AWS_PROFILE', 'itgithubuser')
    s3_client = boto3.client('s3')
    marker=''
    object_count=0
    while True:
        s3_objects = s3_client.list_objects(
            Bucket='itvflightsdata',
            Marker=marker,
            MaxKeys=200
        ).get('Contents']
        if not s3_objects:
            break
        object_count += len(s3_objects)
        marker=s3_objects[-1]['Key']
        print(marker)
    print(object_count)
        
# get size of s3 objects using marker

    pip install hurry.filesize
    from hurry.filesize import size

    import boto3
    import os
    os.environ.setdefault('AWS_PROFILE', 'itgithubuser')
    s3_client = boto3.client('s3')
    marker=''
    object_size=0.0
    while True:
        s3_objects = s3_client.list_objects(
            Bucket='itvflightsdata',
            Marker=marker,
            MaxKeys=200
        ).get('Contents']
        if not s3_objects:
            break
        for s3_object in s3_objects:
            object_size +=s3_object['Size']
        marker=s3_objects[-1]['Key']
        print(marker)
    print(size(object_size))