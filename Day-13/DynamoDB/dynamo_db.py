# Yeh code AWS DynamoDB mein ek naya table banata hai. Neeche code ke har hisse ko Hindi mein explain kiya gaya hai:

import boto3

# boto3 ko import karna
dynamodb = boto3.resource('dynamodb')  # DynamoDB ke resource ko initialize karna

# DynamoDB table create karna
table = dynamodb.create_table(
    TableName='heydevopsmonk',  # Table ka naam
    KeySchema=[              # Primary key aur secondary key ke schema
        {
            'AttributeName': 'username',  # Primary key
            'KeyType': 'HASH'             # HASH type (partition key)
        },
        {
            'AttributeName': 'last_name',  # Secondary key
            'KeyType': 'RANGE'             # RANGE type (sort key)
        }
    ],
    AttributeDefinitions=[    # Attributes ke definitions
        {
            'AttributeName': 'username',   # Primary key
            'AttributeType': 'S'           # String type
        },
        {
            'AttributeName': 'last_name',  # Secondary key
            'AttributeType': 'S'           # String type
        },
    ],
    ProvisionedThroughput={   # Capacity units
        'ReadCapacityUnits': 5,   # Read capacity units
        'WriteCapacityUnits': 5   # Write capacity units
    }
)

# Table ke existence ka wait karna
table.wait_until_exists()

# Table ke baare mein kuch data print karna
print(table.item_count)  # Total items in the table
