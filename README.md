# aws-slack-notifier

This project provisions an **AWS Lambda** function that listens to **EC2 instance state changes** and sends formatted **notifications to Slack** via a webhook.

**Expected output in Slack Workspace:** 

![Image](https://github.com/user-attachments/assets/449a2a31-164c-4422-aa5d-1f2b8cbbcd72)

The infrastructure is defined using [Terraform](https://www.terraform.io/), and the Lambda function is written in Python. This is a concise, real-world serverless monitoring tool and a demonstration of Infrastructure as Code (IaC) best practices.

---

## 🔧 Features

- AWS Lambda triggered via **EventBridge** on EC2 state changes
- Slack integration using **webhook** with secure secret management (AWS Secrets Manager)
- Clean and modular Terraform setup (split `.tf` files)
- Single-command deployment via `deploy.sh`

---

---

## 🧩 Project Files

| File / Folder            | Purpose                                                             |
|--------------------------|---------------------------------------------------------------------|
| `lambda/`                | Contains the Python Lambda function code (`main.py`)                |
| `infrastructure/`        | Contains all Terraform configuration files                          |
| `provider.tf`            | Configures AWS provider and region                                  |
| `variables.tf`           | Declares required input variables                                   |
| `lambda.tf`              | Defines the Lambda function and its deployment package              |
| `iam.tf`                 | IAM role and policy allowing Lambda to be executed and read secrets |
| `events.tf`              | EventBridge rule to trigger Lambda on EC2 instance state changes    |
| `outputs.tf`             | Provides outputs (Lambda function name, EventBridge rule ARN)       |
| `terraform.tfvars`       | Optional: User-defined variable values                              |
| `lambda.zip`             | Auto-generated Lambda package (ignored by Git)                      |
| `deploy.sh`              | Bash script to zip Lambda and run `terraform apply`                 |
| `.gitignore`             | Git exclusions to avoid committing sensitive and generated files    |
| `README.md`              | This documentation                                                  |



---

## 🚀 Deployment

1. Set up a Slack Incoming Webhook and save the URL.
2. Store the webhook in **AWS Secrets Manager** under the name `slack-webhook` with key `SLACK_WEBHOOK_URL`.
3. Clone the repository: 
```bash
git clone https://github.com/janphilippgutt/aws-slack-notifier.git
cd aws-slack-notifier
```
4. Run the deploy script:

```bash
./deploy.sh
```

Your Lambda will now send EC2 state change notifications (start, stop) to your Slack channel.

🔐 Security Notes

    Webhook secrets are securely fetched from Secrets Manager, never hardcoded.

    IAM permissions are scoped minimally for Lambda to access only required services.

🧱 Related Projects

Check out my [aws_backend_setup](https://github.com/janphilippgutt/aws-backend-setup) project — it shows how to:

    Store Terraform state remotely in S3

    Enable state locking using DynamoDB

You can combine both projects to build a complete, production-grade IaC pipeline.

📚 Skills Demonstrated

    AWS Lambda, IAM, EventBridge, Secrets Manager

    Terraform (provider config, IAM roles, Lambda packaging)

    Python (working with AWS SDKs and webhooks)

    Automation with Bash (deploy.sh)

    Git versioning and .gitignore best practices

📌 To Do / Next Steps

    Extend notifications to cover other AWS services (e.g., RDS events, S3 object creation)

    Add automated CI/CD deployment via GitHub Actions


---

## 👥 Contributors

This project shows commits from two GitHub users. Both accounts belong to me:

- [`janphilippgutt`](https://github.com/janphilippgutt) – **primary account**, used for publishing and maintaining portfolio projects
- [`TechWith5000`](https://github.com/TechWith5000) – development-stage account used during early implementation

This structure helped me separate clean production commits from experimental development during the project.


📄 License

MIT