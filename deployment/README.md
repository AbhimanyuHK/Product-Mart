## Deployment

- **Terraform Code**:
  - **main.tf**: Defines the resources to be created, including IAM roles for Glue and Lambda, and an MSK cluster.
  - **variables.tf**: Contains variable definitions for configurable parameters such as AWS region, S3 bucket name, subnet IDs, and security group ID.
  - **outputs.tf**: Specifies the outputs to be exported after the Terraform run, such as ARNs for the Glue role, Lambda role, and MSK cluster.

- **GitHub Actions Code**:
  - **deploy_lambda.yml**: Defines a GitHub Actions workflow to deploy the Lambda function. It packages the Lambda function code and updates the existing Lambda function in AWS.
  - **deploy_glue.yml**: Defines a GitHub Actions workflow to deploy the Glue job. It uploads the Glue job script to an S3 bucket and updates the Glue job configuration.
  - **deploy_infrastructure.yml**: Defines a GitHub Actions workflow to deploy the infrastructure using Terraform. It initializes Terraform and applies the configuration.

### Usage

1. **Set Up GitHub Secrets**:
   - Add your AWS credentials (`AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`) to the secrets in your GitHub repository.

2. **Configure GitHub Actions**:
   - Ensure the `.yml` files are correctly placed in `.github/workflows/` directory within your repository.

3. **Run Terraform Manually (Optional)**:
   - Initialize and apply the Terraform configuration manually to set up the infrastructure.
     ```bash
     cd deployment/infrastructure/terraform
     terraform init
     terraform apply -auto-approve
     ```

4. **Push Changes to GitHub**:
   - Push your changes to the `main` branch to trigger the GitHub Actions workflows for deploying Lambda, Glue, and infrastructure.

This setup allows for automated deployment and infrastructure management using Terraform and GitHub Actions, ensuring a streamlined and repeatable deployment process.
