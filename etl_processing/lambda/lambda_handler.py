import json
import boto3
import kafka_config

def lambda_handler(event, context):
    glue_client = boto3.client('glue')
    job_name = kafka_config.GLUE_JOB_NAME

    try:
        response = glue_client.start_job_run(JobName=job_name)
        return {
            'statusCode': 200,
            'body': json.dumps(f'Successfully started Glue job: {response["JobRunId"]}')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error starting Glue job: {str(e)}')
        }
