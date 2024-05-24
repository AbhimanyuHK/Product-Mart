variable "aws_region" {
  description = "The AWS region to create resources in."
  default     = "us-west-2"
}

variable "s3_bucket_name" {
  description = "The name of the S3 bucket."
}

variable "subnet_ids" {
  description = "The list of subnet IDs."
  type        = list(string)
}

variable "security_group_id" {
  description = "The security group ID."
}
