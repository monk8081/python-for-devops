import logging
import boto3
from botocore.exceptions import ClientError
import os

def upload_file(file_name, bucket, object_name=None):
    # Agar S3 object_name specify nahi kiya gaya hai, to file_name ka istemal karna
    if object_name is None:
        object_name = os.path.basename(file_name)
    # File ko upload karna
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

# File ko S3 bucket mein upload karna
upload_file("/c/Users/Manish Allahbadia/Downloads/Telegram Desktop/DevOps_Fresher_Resume.docx", "singpssingh")


# Is code mein, upload_file function ke zariye ek file ko AWS S3 bucket mein upload kiya jata hai.
# Agar S3 object ka naam specify nahi kiya gaya hai, to file ka base name (os.path.basename(file_name)) ka istemal hota hai.
# Phir upload_file function ko call karke file ko S3 bucket mein upload kiya jata hai.