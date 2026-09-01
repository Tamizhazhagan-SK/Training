import boto3

source_file_path = "C:/Users/SKTamizhazhagan/OneDrive - BMW Techworks India Private Limited/Training/AWS/DAY-36/small-potato/src/modules/data/bmw_customers.csv"
bucket_name = 'small-potato'
s3_file_path = 'friday/bmw_customers.csv'
s3_client = boto3.client('s3', region_name='us-west-2')

try:
    s3_client.upload_file(source_file_path, bucket_name, s3_file_path)
    print(f"Successfully uploaded {source_file_path} to s3://{bucket_name}/{s3_file_path}")
except Exception as e:
    print(f"Error uploading file: {e}")