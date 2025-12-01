# main.tf

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region     = "us-west-2"
  access_key = "test"
  secret_key = "test"

  # LocalStack 本地测试用
  endpoints {
    dynamodb = "http://localhost:4566"
    lambda   = "http://localhost:4566"
  }
}

########################
# DynamoDB Table
########################
resource "aws_dynamodb_table" "url_table" {
  name         = "url_table"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "id"

  attribute {
    name = "id"
    type = "S"
  }
}

########################
# Lambda Function
########################
resource "aws_lambda_function" "create_function" {
  function_name = "CreateFunction"
  handler       = "app.handler"
  runtime       = "python3.12"

  filename         = "lambda_package.zip"  # 先把 app.py 打包
  source_code_hash = filebase64sha256("lambda_package.zip")

  environment {
    variables = {
      TABLE_NAME = aws_dynamodb_table.url_table.name
    }
  }
}
