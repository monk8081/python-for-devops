# Yeh code bhi AWS DynamoDB table ke saath interaction karta hai. 
import boto3
# boto3 ko import karna

dynamodb = boto3.resource('dynamodb')  # DynamoDB ke resource ko initialize karna

# 'heydevops' naam ke table ko select karna
table = dynamodb.Table('heydevopsmonk')

# Table ka creation date and time print karna
print(table.creation_date_time)

# Ek item (row) ko update karna table mein
table.update_item(
    Key={
        'username': 'Monk',  # Primary key ke value
        'last_name': 'Singh'       # Secondary key ke value
    },
    UpdateExpression='SET age = :val1',  # UpdateExpression batata hai kya update karna hai
    ExpressionAttributeValues={           # ExpressionAttributeValues mein values specify kiye jate hain
        ':val1': 26                       # :val1 placeholder ka value specify kiya gaya hai
    }
)
