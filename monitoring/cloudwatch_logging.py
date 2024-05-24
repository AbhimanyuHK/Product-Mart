import boto3
import logging
import os
from datetime import datetime

# Configure logging
LOG_GROUP_NAME = 'ETLProcessLogs'
LOG_STREAM_NAME = 'ETLProcessStream'
LOG_LEVEL = logging.INFO

logging.basicConfig(level=LOG_LEVEL)
logger = logging.getLogger()

# Configure CloudWatch Logs
client = boto3.client('logs')
response = client.create_log_stream(
    logGroupName=LOG_GROUP_NAME,
    logStreamName=LOG_STREAM_NAME
)

def log_to_cloudwatch(message):
    timestamp = int(datetime.now().timestamp() * 1000)
    log_event = {
        'logGroupName': LOG_GROUP_NAME,
        'logStreamName': LOG_STREAM_NAME,
        'logEvents': [
            {
                'timestamp': timestamp,
                'message': message
            }
        ]
    }
    response = client.put_log_events(**log_event)
    return response

if __name__ == "__main__":
    test_message = "ETL Process started."
    response = log_to_cloudwatch(test_message)
    print("Logged to CloudWatch:", test_message)
