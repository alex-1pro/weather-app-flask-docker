import datetime

import boto3
from boto3.dynamodb.conditions import Key, Attr

MAX_BACKUPS = 3

dynamo = boto3.client('dynamodb')
dynamodb_test = boto3.resource('dynamodb')
table_test = dynamodb_test.Table('weather')
print(table_test)


# response = table_test.query(
#         KeyConditionExpression=Key('city_name').eq('Tel Aviv')
#     )
# items = response['Items']

# response = table_test.get_item(
#     Key={
#         'city_name': 'Tel Aviv'
#     }
# )
# items = response['Items']
# print(items)

def lambda_handler(event, context):
    if 'TableName' not in event:
        raise Exception("No table name specified.")
    table_name = event['TableName']
    print(table_name)

    # response = table_test.query(
    #     KeyConditionExpression=Key('city_name').eq('Tel Aviv')
    # )
    # items = response['Items']
    # print(items)
    print(table_test)
    response = table_test.query(
        KeyConditionExpression=Key('city_name').eq('Tel Aviv')
    )
    items = response['Items']
    items = response['Items']
    print(items)

    create_backup(table_name)
    delete_old_backups(table_name)


def create_backup(table_name):
    print("Backing up table:", table_name)
    backup_name = table_name + '-' + datetime.datetime.now().strftime('%Y%m%d%H%M%S')

    response = dynamo.create_backup(
        TableName=table_name, BackupName=backup_name)

    print(response)


def delete_old_backups(table_name):
    print("Deleting old backups for table:", table_name)

    backups = dynamo.list_backups(TableName=table_name)

    backup_count = len(backups['BackupSummaries'])
    print('Total backup count:', backup_count)

    if backup_count <= MAX_BACKUPS:
        print("No stale backups. Exiting.")
        return

    sorted_list = sorted(backups['BackupSummaries'],
                         key=lambda k: k['BackupCreationDateTime'])

    old_backups = sorted_list[:MAX_BACKUPS]

    for backup in old_backups:
        arn = backup['BackupArn']
        print("ARN to delete: " + arn)
        deleted_arn = dynamo.delete_backup(BackupArn=arn)
        status = deleted_arn['BackupDescription']['BackupDetails']['BackupStatus']
        print("Status:", status)

    return
