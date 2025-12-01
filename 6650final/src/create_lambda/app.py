import os
import json
import boto3

# Get the table name from environment variables
TABLE_NAME = os.getenv("TABLE_NAME", "url_table")

# Connect to DynamoDB running on LocalStack
dynamodb = boto3.resource(
    "dynamodb",
    region_name="us-west-2",
    endpoint_url="http://localhost:4566"
)

table = dynamodb.Table(TABLE_NAME)

def handler(event, context):
    """
    Lambda entry function
    event: contains HTTP request information
    context: Lambda runtime context (can be ignored)
    """
    print("EVENT =", event)

    try:
        # Read JSON data from event body
        body = json.loads(event.get("body", "{}"))
        url = body.get("url")

        if not url:
            return {
                "statusCode": 400,
                "body": json.dumps({"message": "Missing URL"})
            }

        # Generate a simple ID (can replace with more complex short URL logic)
        short_id = "123"

        # Write to DynamoDB
        table.put_item(Item={"id": short_id, "original_url": url})

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Saved", "short_id": short_id, "url": url})
        }

    except Exception as e:
        print("Error:", e)
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "Internal server error", "error": str(e)})
        }


