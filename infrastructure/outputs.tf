output "lambda_function_name" {
  value       = aws_lambda_function.slack_notifier.function_name
  description = "Name of the Slack notifier Lambda function"
}

output "eventbridge_rule_arn" {
  value       = aws_cloudwatch_event_rule.ec2_state_change.arn
  description = "ARN of the EventBridge rule triggering the Lambda"
}
