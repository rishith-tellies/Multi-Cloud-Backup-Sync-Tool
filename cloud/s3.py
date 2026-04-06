import boto3

s3 = boto3.client(
    's3',
    aws_access_key_id="AWS_ACCESS_KEY_ID",  # Replace with your aws_access_key_id
    aws_secret_access_key="AWS_SECRET_ACCESS_KEY"   # Replace with your aws secret_access_key
)

BUCKET_NAME = "AWS_BUCKET_NAME"  # Replace with your bucket name

def upload_to_s3(file_path, key):
    s3.upload_file(file_path, BUCKET_NAME, key)