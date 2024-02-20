# Yeh code AWS S3 mein ek naya bucket create karta hai. Neeche code ke har hisse ko Hindi mein explain kiya gaya hai
import boto3
import logging
from botocore.exceptions import ClientError

def create_bucket(bucket_name, region=None):
    # Bucket create karna
    try:
        if region is None:
            s3_client = boto3.client('s3')  # Default region mein client initialize karna
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)  # Specific region mein client initialize karna
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                     CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True

# Bucket create function ko call karna
create_bucket("singpssingh", "us-west-1")
  # Bucket name aur region specify karna

# iss code mein, create_bucket function ke zariye AWS S3 mein ek naya bucket banaya jata hai.
# Agar koi exception aati hai toh wo logging.error ke zariye log ki jati hai.
# Phir create_bucket function ko call karke naya bucket create kiya jata hai, 
# jisme bucket ka naam aur region specify kiya gaya hai.
