import boto3
import botocore
import requests
from pprint import pprint
from boto3.dynamodb.conditions import Key, Attr
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
sess = boto3.Session(region_name='us-east-1')
ddb = sess.client('dynamodb', **AWS_S3_CREDS)

table = 'weather'


# item = {
#     'city_name': {
#         'S': 'Ramat Gan'
#     },
#     'date': {
#         'S': '23/03/2022'
#     },
#     'weather': {
#         'S': 'Cloud'
#     }
# }


# ddb.put_item(TableName=table, Item=item)

def adding_item_db(daily, city_name, country):
    print(daily, '\n', city_name, '\n', country)
    print(daily[0]["day_week"])
    print(f'{daily[0]["day_week"]}')
    item = {
        'city_name': {
            'S': city_name
        },
        'country': {
            'S': country
        },
        'day_week': {
            'S': f'{daily[0]["day_week"]}'
            # 'date': daily[0]["t_date"].day,
            # 'month': daily[0]["t_date"].strftime("%B"),
            # 'temp': daily[0]["current_temp"],
            # 'description': daily[0]["description"]
        }
    }

    ddb.put_item(TableName=table, Item=item)


dynamodb = boto3.Session(region_name='us-east-1')
dynamo_test = dynamodb.resource('dynamodb', **AWS_S3_CREDS)
table_test = dynamo_test.Table('weather')
print(table_test)
#
# response = table_test.query(
#     KeyConditionExpression=Key('city_name').eq('Tel Aviv')
# )
# items = response['Items']
response = table_test.get_item(
    Key={
        'city_name': 'Tel Aviv'
    }
)
items = response['Item']
print(items)