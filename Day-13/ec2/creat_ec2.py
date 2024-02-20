import boto3

# Set up the EC2 client
ec2 = boto3.client('ec2', region_name='us-east-1',
                    aws_access_key_id='AKIA6KX7OYXMLPE4MLGG',
                    aws_secret_access_key='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')

# Create key pair
key_pair_response = ec2_client.create_key_pair(KeyName='monkita')
print("Key pair created:", key_pair_response['KeyName'])




# Define parameters for the new instance
instance_params = {
    'ImageId': 'ami-0c7217cdde317cfec',  # Specify the AMI ID of the image you want to use
    'InstanceType': 't2.micro',  # Specify the instance type
     'KeyName': 'monkita',  # Specify the key pair name
    'MinCount': 1,  # Minimum number of instances to launch
    'MaxCount': 1,  # Maximum number of instances to launch
    # You can add more parameters as needed, such as SecurityGroups, SubnetId, etc.
}






# Launch the EC2 instance
response = ec2.run_instances(**instance_params)




# Print the instance ID
print("Instance ID:", response['Instances'][0]['InstanceId'])     



