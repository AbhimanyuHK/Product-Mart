import boto3

client = boto3.client('cloudwatch')

def create_alarm(alarm_name, namespace, metric_name, threshold, period=300, evaluation_periods=1):
    response = client.put_metric_alarm(
        AlarmName=alarm_name,
        MetricName=metric_name,
        Namespace=namespace,
        Statistic='Sum',
        Period=period,
        EvaluationPeriods=evaluation_periods,
        Threshold=threshold,
        ComparisonOperator='GreaterThanOrEqualToThreshold',
        AlarmActions=[
            'arn:aws:sns:your-region:your-account-id:your-sns-topic'
        ],
        AlarmDescription='Alarm when the ETL process metric exceeds the threshold',
        Dimensions=[
            {
                'Name': 'ETLProcess',
                'Value': 'ETL'
            },
        ],
    )
    return response

if __name__ == "__main__":
    alarm_name = 'ETLProcessAlarm'
    namespace = 'ETLProcessMetrics'
    metric_name = 'RecordsProcessed'
    threshold = 1000
    response = create_alarm(alarm_name, namespace, metric_name, threshold)
    print("Alarm created in CloudWatch:", response)
