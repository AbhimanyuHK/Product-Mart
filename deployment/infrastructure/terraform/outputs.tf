output "glue_role_arn" {
  description = "The ARN of the Glue role."
  value       = aws_iam_role.glue_role.arn
}

output "lambda_role_arn" {
  description = "The ARN of the Lambda role."
  value       = aws_iam_role.lambda_role.arn
}

output "kafka_cluster_arn" {
  description = "The ARN of the MSK cluster."
  value       = aws_msk_cluster.kafka_cluster.arn
}
