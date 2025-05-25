#!/bin/bash

set -e  # Exit on any error

echo "📦 Zipping Lambda function..."
cd lambda
zip -r ../infrastructure/lambda.zip . > /dev/null
cd ..

echo "🚀 Running Terraform apply..."
cd infrastructure
terraform apply -auto-approve
cd ..

echo "✅ Deployment complete!"
