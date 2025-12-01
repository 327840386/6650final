#!/usr/bin/env bash
set -e
# 启动 localstack
docker compose -f docker-compose.yml up -d


# 创建 DynamoDB 表
aws --endpoint-url=http://localhost:4566 dynamodb create-table \
--table-name url_table \
--attribute-definitions AttributeName=short_code,AttributeType=S \
--key-schema AttributeName=short_code,KeyType=HASH \
--billing-mode PAY_PER_REQUEST


# 使用 SAM local 启动 API
cd ../src
sam build
sam local start-api --docker-network host --port 3000