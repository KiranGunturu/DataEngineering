import boto3
import math
from datetime import datetime
import time
import xml.etree.ElementTree as ET
import xml.dom.minidom as dom

ET.register_namespace("", 'http://www.dealer.com/pega/ro');
baseXml = '<?xml version="1.0" encoding="UTF-8"?><PegaRepairOrder xmlns="http://www.dealer.com/pega/ro"></PegaRepairOrder>'


collectedmessages = []
queue_url = 'https://sqs.us-east-2.amazonaws.com/923737072554/ro-sqs'
noofMessages = 0
batchSize = 20 # make it 500

# Get 10 messages from queue
def receiveMessages(sqs, queue_url): 
    response = sqs.receive_message(
        QueueUrl=queue_url,
        AttributeNames=[
            'SentTimestamp'
        ],
        MaxNumberOfMessages=10,
        MessageAttributeNames=[
            'All'
        ],
        VisibilityTimeout=20,
        WaitTimeSeconds=20
    )
    return response

# Delete received message from queue
def deleteHandle(receipt_handle, sqs, queue_url):
    sqs.delete_message(
        QueueUrl=queue_url,
        ReceiptHandle=receipt_handle
    )

def stripXML(str):
  if(len(str) > 0):
    res = str.replace('<?xml version="1.0" encoding="UTF-8"?>','')
    res = res.replace(' xmlns="http://www.test.com/pega/ro"','')
    return res
  else: 
    return str
  
   
def extractRepairOrder(str):
  #print(str)
  if(len(str) > 0):
    rt = ET.fromstring(str)
    print(rt)
    ro = rt.find('./{http://www.test.com/pega/ro}RepairOrder')
    print(ro)
    return ro;
  else: 
    return '';
    
def prepareFullXML(batch):
    fullxml = ET.fromstring(baseXml)
    for st in batch:
      #print(xml);
      result = extractRepairOrder(st)
      #print(result)
      fullxml.find('.').append(result)
    fullxml= ET.tostring(fullxml, encoding='utf8');
    
    #fullxml= fullxml.decode(encoding='UTF-8').replace("'", '"')
    #fulldom = dom.parseString(fullxml)
    print(" -------------------------------- dom prints after this")
    fullxml = fullxml.decode('utf-8')
    xml_tree = dom.parseString(fullxml)
    xml_pretty_str = xml_tree.toprettyxml()
    return xml_pretty_str

def batchXML(batch):
    str = ''
    for xmlStr in batch: 
        str = str + stripXML(xmlStr) + "\r\n"
    return str

# Process received message from queue
def processQueue(sqs, queue_url, noofMessages):
    print("Process queue start for " + str(noofMessages))
    while(len(collectedmessages) < noofMessages):
        response = receiveMessages(sqs, queue_url)
        #print(response) 
        for msg in response["Messages"]:
            if(len(collectedmessages) < noofMessages):
                collectedmessages.append(msg["Body"]);
                #deleteHandle(msg['ReceiptHandle'], sqs, queue_url)
        #print(str(len(collectedmessages)) + " of messages read.")
def storeInS3(strToWrite):
    BUCKET_NAME = 'dbsro'
    PREFIX = 'landing/'
    Filename = time.strftime('RO_'+"%Y%m%d"+'_'+"%H%M%S"+'.XML')
    s3 = boto3.resource('s3')
    s3.Object(BUCKET_NAME, PREFIX+ Filename).put(Body=strToWrite)

    
        
def writeTos3inBatches(batchSize, collectedmessages): 
    batchArray = [collectedmessages[i:i + batchSize] for i in range(0, len(collectedmessages), batchSize)]
                            # [[1,2], [3,4]]
    print("Total files to write : " + str(len(batchArray)));
    for batch in batchArray:
        print(str(len(batch)) + " is number of messages in this file" + str(len(batchArray)))
        #strToWrite = ",".join(batch)
        # choose method to generate batchXML or prepareFullXML
        #strToWrite = batchXML(batch)
        print("prepareFullXML call start : len is " + str(len(batch)))
        strToWrite = prepareFullXML(batch)
        print("prepareFullXML call end : len is " + str(len(batch)))
        storeInS3(strToWrite)
    

# Start here
def lambda_handler(event, context):
    sqs = boto3.client('sqs')
    queue_url = 'https://sqs.us-east-2.amazonaws.com/923737072554/ro-sqs'
    # This reads 500 messages in one go, modify as needed
    attribs  = sqs.get_queue_attributes(
        QueueUrl=queue_url,
        AttributeNames=['ApproximateNumberOfMessages', 'ApproximateNumberOfMessagesNotVisible']
     )
    noofMessages = int(attribs['Attributes']['ApproximateNumberOfMessages']) + int(attribs['Attributes']['ApproximateNumberOfMessagesNotVisible'])
    
    print("no of messages are " + str(noofMessages))
    noofMessages = int(math.floor(noofMessages/batchSize))*batchSize
    print("no of messages after are: " + str(noofMessages))
    #print(maxLoops)
    
    try:
        #for n in range(maxLoops):
        print("inside try")
        processQueue(sqs, queue_url, noofMessages)
        #print("Batch No. "+ str(n+1) +" completed")
        writeTos3inBatches(batchSize, collectedmessages)
        #print(",".join(collectedmessages)) 
    except Exception as e:
      print(e)



