import json
import boto3
from pymongo import MongoClient
from bson import json_util
from botocore.exceptions import NoCredentialsError, ClientError

try: 
    # Connect to MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    db = client["weather_db"]
    collection = db["London_Forecast"]

    # Fetch all documents from MongoDB (including _id)
    documents = list(collection.find())

    # Export to JSON file
    with open("weather_data.json", "w") as f:
        json.dump(documents, f, default=json_util.default, indent=4)
    print("Data exported to weather_data.json")

    
    # Upload to S3
    s3_client = boto3.client('s3', region_name='eu-central-1')

    
    s3_client.upload_file(
        Filename="weather_data.json",
        Bucket="se-data-with-ai-etl-project",
        Key="se-data-folder/se-rory/weather_data.json"
    )

    print("Uploaded to S3")

except NoCredentialsError:
    print("AWS credentials not found.")

except ClientError as e:
    print(f"AWS Error: {e}")

except Exception as e:
    print(f"ERROR: {e}")

