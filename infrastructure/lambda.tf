resource "aws_lambda_function" "slack_notifier" {
  function_name = "slack_notifier_lambda"
  filename      = "${path.module}/lambda.zip"
  source_code_hash = filebase64sha256("${path.module}/lambda.zip")
  handler       = "main.lambda_handler"
  runtime       = "python3.12"

  role = aws_iam_role.lambda_exec.arn

  environment {
    variables = {
      SLACK_WEBHOOK_URL = var.slack_webhook_url
    }
  }
}