# Yeh code ek AWS DynamoDB table ke saath interaction karta hai.

import boto3

# boto3 ko import karna
dynamodb = boto3.resource('dynamodb')  # DynamoDB ke resource ko initialize karna

# 'heydevops' naam ke table ko select karna
table = dynamodb.Table('heydevopsmonk')

# Table ka creation date and time print karna
print(table.creation_date_time)

# Ek item (row) ko table mein insert karna
table.put_item(
   Item={
        'username': 'Monk',
        'first_name': 'Manish',
        'last_name': 'Singh',
        'age': 25,
        'account_type': 'standard_user',
    }
)

# Table se ek item (row) retrieve karna
response = table.get_item(
    Key={
        'username': 'janedoe',  # Primary key ke value
        'last_name': 'Doe'       # Secondary key ke value
    }
)

# Response se item (row) nikalna
item = response['Item']

# Item (row) ko print karna
print(item)



# Is code mein, boto3 library ko import kiya gaya hai aur uska use DynamoDB ke saath interaction karne ke liye kiya gaya hai. 
# heydevops naam ke table ko select kiya gaya hai. 
# Fir ek item ko table mein insert kiya gaya hai put_item method ke zariye. Uske baad,
# ek item ko table se retrieve kiya gaya hai get_item method se. Aur retrieved item ko print kiya gaya hai.
