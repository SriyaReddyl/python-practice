""" import boto3 # The official AWS SDK for Python. It lets you talk to AWS services (S3, EC2, DynamoDB, etc.) from code
s3 = boto3.client("s3") # Creates a client object for the S3 service. It uses your AWS credentials automatically, found via environment variables, ~/.aws/credentials, or an IAM role. Every S3 operation is a method on this s3 object.
response = s3.list_buckets() # Makes an API call to AWS asking for all S3 buckets in your account. The result is stored in response as a Python dictionary
print(response) # 
 """
 
import boto3
s3 = boto3.client("s3")
response = s3.list_buckets()
for bucket in response["Buckets"]: # Loops over the list stored under the "Buckets" key. On each iteration, bucket is one dictionary representing a single bucket
    print(bucket["Name"])