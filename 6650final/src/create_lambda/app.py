import os
import json
import boto3

dynamodb = boto3.resource(
    "dynamodb",
    region_name="us-west-2",
    endpoint_url="http://localhost:4566"  # 指向 LocalStack
)

table = dynamodb.Table("url_table")

def handler(event, context):
    print("EVENT =", event)
    
    body = json.loads(event["body"])
    url = body["url"]

    # 注意这里的 key 名必须是表定义里的 short_id
    table.put_item(Item={"short_id": "123", "original_url": url})

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Saved", "url": url})
    }

