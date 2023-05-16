import boto3

instance_id = "i-049bf89877891eb9a"


ec2 = boto3.client('ec2')

response = ec2.stop_instances(
        InstanceIds=[
            instance_id
        ]
        
    )    
            
            

print(response)