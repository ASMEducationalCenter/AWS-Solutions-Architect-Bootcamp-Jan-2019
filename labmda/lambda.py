## This is the AWS SDK for python
import boto3
def lambda_handler(event, context):

    
    client=boto3.client('ec2')
    
    
    ## this describes the EC2 instances in your region
    response=client.describe_instances()
    
    
    for reservation in response["Reservations"]:
    
    	for instance in reservation["Instances"]:
    
            	print(instance["InstanceId"] + "stopping")
    
            	id=[instance["InstanceId"]]
                
                ## this is the line that does the actual stopping of the EC2 instances
            	client.stop_instances(InstanceIds=id)
