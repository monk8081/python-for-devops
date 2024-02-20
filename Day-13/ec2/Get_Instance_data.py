import boto3
from collections import defaultdict
ec2 = boto3.resource('ec2')

# Chal rahi sabhi instances ke liye jaankari collect karna
running_instances = ec2.instances.filter(Filters=[{

    'Name': 'instance-state-name',
    'Values': ['running']}])

# Ek default dictionary banakar EC2 instances ki jaankari collect karna
ec2info = defaultdict()
for instance in running_instances:
    # Instance ke tags se Name attribute nikalna
    for tag in instance.tags:
        if 'Name'in tag['Key']:
            name = tag['Value']
    # Instance ki jaankari ko dictionary mein add karna         
    ec2info[instance.id] = {
        'Name': name,
        'Type': instance.instance_type,
        'State': instance.state['Name'],
        'Private IP': instance.private_ip_address,
        'Public IP': instance.public_ip_address,
        'Launch Time': instance.launch_time
        }

# Chune hue attributes ke liye loop chalana aur print karna
attributes = ['Name', 'Type', 'State', 'Private IP', 'Public IP', 'Launch Time']
for instance_id, instance in ec2info.items():
    for key in attributes:
        print("{0}: {1}".format(key, instance[key]))
    print("------")


    # Is code mein, sabhi running EC2 instances ki jaankari collect ki jati hai,
    # fir ek dictionary mein store ki jati hai.
    # Phir dictionary ke har item ko loop ke zariye iterate kiya jata hai aur chune hue attributes ke liye unki values print ki jati hai.