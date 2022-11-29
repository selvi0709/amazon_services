import boto3
from uuid import uuid4

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
student_table = dynamodb.Table('students')


def lambda_handler(event, context):
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    print(f"Printing bucket name: {bucket_name}")
    file_name = event['Records'][0]['s3']['object']['key']
    file_object = s3.get_object(Bucket=bucket_name, Key=file_name)
    file_content = file_object['Body'].read().decode('utf-8')
    students = file_content.split("\n")

    for i in range(1, len(students) - 1):
        data = students[i].split(',')
        print(f'printing id {data[0]}')
        print(f'printing name {data[1]}')
        student_table.put_item(
            Item={
                "id": int(data[0]),
                "name": str(data[1])
            }
        )
