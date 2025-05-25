def lambda_handler(event, context):
    # 1. Pull in config
    webhook_url = os.environ.get("SLACK_WEBHOOK_URL")

    # 2. Parse the event
    instance_id = event.get("detail", {}).get("instance-id", "unknown")
    state = event.get("detail", {}).get("state", "unknown")

    # 3. Construct the message
    message = f"EC2 Instance {instance_id} is now {state}"

    # 4. Send HTTP POST request
    req = urllib.request.Request(
        webhook_url,
        data=json.dumps({"text": message}).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )
    urllib.request.urlopen(req)

    # 5. Return response
    return {
        "statusCode": 200,
        "body": json.dumps("Notification sent")
    }
