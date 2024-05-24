import boto3

client = boto3.client('cloudwatch')

def put_metric_data(namespace, metric_name, value, unit='Count'):
    response = client.put_metric_data(
        Namespace=namespace,
        MetricData=[
            {
                'MetricName': metric_name,
                'Dimensions': [
                    {
                        'Name': 'ETLProcess',
                        'Value': 'ETL'
                    },
                ],
                'Value': value,
                'Unit': unit
            },
        ]
    )
    return response

if __name__ == "__main__":
    namespace = 'ETLProcessMetrics'
    metric_name = 'RecordsProcessed'
    value = 100
    response = put_metric_data(namespace, metric_name, value)
    print("Metric data sent to CloudWatch:", response)
