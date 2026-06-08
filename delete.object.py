import boto3

s3_client = boto3.client('s3', region_name='eu-central-1')

response = s3_client.list_objects_v2(
    Bucket='se-data-with-ai-etl-project',
    Prefix='se-data-folder/se-sakib/'
)

if 'Contents' in response:
    for obj in response['Contents']:
        s3_client.delete_object(
            Bucket='se-data-with-ai-etl-project',
            Key=obj['Key']
        )
        print(f"Deleted: {obj['Key']}")
else:
    print("No objects found!")

print("Done!")