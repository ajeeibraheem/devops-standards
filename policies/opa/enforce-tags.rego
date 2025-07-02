package policy.enforce_tags

deny[msg] {
  input.resource_type == "aws_instance"
  not input.tags["owner"]
  msg := "Missing required tag: owner"
}

deny[msg] {
  input.resource_type == "aws_instance"
  not input.tags["cost_center"]
  msg := "Missing required tag: cost_center"
}
