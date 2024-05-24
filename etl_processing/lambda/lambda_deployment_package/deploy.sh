#!/bin/bash

# Package and deploy the Lambda function
zip -r lambda_function.zip .

aws lambda update-function-code \
    --function-name start-glue-job \
    --zip-file fileb://lambda_function.zip

echo "Lambda function deployed successfully."
