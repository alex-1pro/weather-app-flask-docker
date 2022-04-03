import boto3
import botocore
import requests
from dotenv import load_dotenv
import os
# path = '/home/alex/Downloads'
#

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")


AWS_S3_CREDS = {
        "aws_access_key_id": AWS_ACCESS_KEY_ID,  # os.getenv("AWS_ACCESS_KEY")
        "aws_secret_access_key": AWS_SECRET_ACCESS_KEY # os.getenv("AWS_SECRET_KEY")
    }
# s3_client = boto3.client('s3',**AWS_S3_CREDS)
#
#
# #s3 = boto3.client('s3')
# s3_client.download_file('alexeyindex.com', 'download/sky.jpg', '/home/alex/Desktop/downtest/client_sky.jpg')


