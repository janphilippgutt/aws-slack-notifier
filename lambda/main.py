import boto3
import json
import urllib.request

def get_slack_webhook():
    secret_name = "slack-webhook"
    region_name = "eu-central-1"

    client = boto3.client("secretsmanager", region_name=region_name)
    get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    secret = json.loads(get_secret_value_response["SecretString"])
    return secret["SLACK_WEBHOOK_URL"]

def lambda_handler(event, context):
    webhook_url = get_slack_webhook()
    if not webhook_url:
        raise ValueError("SLACK_WEBHOOK_URL environment variable not set")

    # Debug: print raw event
    print("Received event:", json.dumps(event))

    # Extract meaningful data
    detail = event.get("detail", {})
    instance_id = detail.get("instance-id", "unknown")
    state = detail.get("state", "unknown")

    message = f"EC2 Instance `{instance_id}` has changed state to *{state}*."

    payload = {
        "text": message
    }

    req = urllib.request.Request(
        webhook_url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )

    try:
        with urllib.request.urlopen(req) as response:
            response_body = response.read()
            print("Slack response:", response_body)
    except Exception as e:
        print("Error sending message to Slack:", str(e))
        raise e

    return {
        "statusCode": 200,
        "body": json.dumps("Notification sent.")
    }
