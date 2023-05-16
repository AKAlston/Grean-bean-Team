import boto3

instance_id = "i-05483a47e32098793"


ec2 = boto3.client('ec2')

response = ec2.stop_instances(
        InstanceIds=[
            instance_id
        ]
        
    )    
            
            

print(response)