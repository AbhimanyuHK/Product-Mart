## ETL Processing

- **etl_processing/lambda/lambda_handler.py**: This AWS Lambda function is used to trigger the AWS Glue job. It uses `boto3` to start the Glue job and returns the job run ID.
- **etl_processing/lambda/lambda_deployment_package/requirements.txt**: Specifies the dependencies for the Lambda function.
- **etl_processing/lambda/lambda_deployment_package/deploy.sh**: Shell script to package and deploy the Lambda function.
- **etl_processing/glue/glue_job.py**: AWS Glue job script written in Python using PySpark. It reads data from Kafka, processes it, and writes it to Snowflake.
- **etl_processing/glue/glue_config.json**: Configuration file for the AWS Glue job, specifying details such as the script location, execution role, and allocated capacity.

### Usage

1. **Deploy Lambda Function**:
   - Navigate to the `etl_processing/lambda/lambda_deployment_package` directory and run the deploy script.
     ```bash
     cd etl_processing/lambda/lambda_deployment_package
     chmod +x deploy.sh
     ./deploy.sh
     ```

2. **Create Glue Job**:
   - Create a new Glue job in the AWS Glue console using the configuration in `glue_config.json`. Upload the `glue_job.py` script to an S3 bucket and specify its location in the Glue job configuration.

3. **Trigger Glue Job with Lambda**:
   - The Lambda function can be triggered manually, or you can set up a CloudWatch event to trigger it on a schedule. The Lambda function will start the Glue job, which will read from Kafka, process the data, and load it into Snowflake.

This setup will allow you to perform ETL processing using AWS Glue and AWS Lambda, reading data from Kafka, transforming it, and loading it into Snowflake for further analysis.
