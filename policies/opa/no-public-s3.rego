package policy.s3_restrictions

deny[msg] {
  input.resource_type == "aws_s3_bucket"
  input.acl == "public-read"
  msg := "S3 bucket must not have public-read ACL"
}

deny[msg] {
  input.resource_type == "aws_s3_bucket"
  input.policy.Statement[_].Effect == "Allow"
  input.policy.Statement[_].Principal == "*"
  msg := "S3 bucket must not allow public access via policy"
}
