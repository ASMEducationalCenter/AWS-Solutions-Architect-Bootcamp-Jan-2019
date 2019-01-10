import boto3
dynamo= boto3.resource('dynamodb',region_name='us-east-1')
table=dynamo.Table('Dynamo-Lambda')


sendDynamo= table.put_item(TableName='Dynamo-Lambda',Item= {"id" : 2 , "Labels": "apple" })
