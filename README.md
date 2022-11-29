# Retrieving data from S3 and moving to RDS DB using EC2 instance - Server based architecture

## Requirements: S3 bucket should be created and file should be uploaded in the S3

- Step 1: Create EC2 instance
- Step 2: Create RDS Database
- Step 3: Install all the dependencies in the EC2 instance machine
- Step 4: Run the python file which will retrieve the data from S3 bucket and transfer the data into RDS

```
Python Installation
    1  sudo apt update
    2  sudo apt install software-properties-common
    3  sudo add-apt-repository ppa:deadsnakes/ppa
    4  sudo apt install python3.9
    5  python3 --version
    6  python3.9 --version
```
```
Installing requirements
   1  sudo apt install python3.9-pip
   2  sudo apt install python3-pip
   3  pip install boto3
```
```
Pymysql Installation
   1  pip install pymysql
```

### Setting env for boto client access

```
   1  export AWS_ACCESS_KEY_ID=AKIA4FVO23**********
   2  export AWS_SECRET_ACCESS_KEY=CUGXRWzWYnh3uMtoY1AD***********
   3  export AWS_DEFAULT_REGION=us-east-1
   4  env | grep "AWS"
```
```
Run python file
   1  python3 file.py

Refer file: ec2_deploy_file.py
```

--------------------------------------------------------------------------------------------------------------

# Retrieving data from S3 and transferring to dynamodb using lambda and trigger functions - Serverless based architecture

## Requirements: S3 bucket should be created, DynamoDB table should be created

- Step 1: Create IAM Role which will have full access to the following services:
    - S3
    - DynamoDB
    - CloudWatch
> Note: Newly created role should be applied for the lambda function
- Step 2: Create Lambda function
- Step 3: Create trigger inside the lambda function for S3 bucket
- Step 4: Add the python file and deploy
- Step 5: After uploading the file inside the S3 bucket, data will be automatically read from S3 and will be loaded inside
the DynamoDB table using the lambda function
- Step 6: Data will be seen inside the DynamoDB table
- Step 7: Additionally we can also watch logs in the CloudWatch service
- Refer file: lambda_deploy_file.py
