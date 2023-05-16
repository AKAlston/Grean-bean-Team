import boto3

instance_id = "i-0b2827b3c091ef05f"


ec2 = boto3.client('ec2')

response = ec2.stop_instances(
        InstanceIds=[
            instance_id
        ]
        
    )    
            
            

print(response)