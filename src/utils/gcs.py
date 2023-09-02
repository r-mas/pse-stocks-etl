"""Google Cloud Storage helper functions"""

# Author: Rey Anthony Masilang


from dotenv import load_dotenv
from os import environ
from google.cloud import storage


__all__ = [
    'upload_to_gcs',
    'delete_object',
]


# Prepare database credentials
load_dotenv('.env')

GCP_PROJECT_NAME = environ.get('GCP_PROJECT_NAME')
GCP_CREDENTIALS_FILE = environ.get('GCP_CREDENTIALS_FILE')


def upload_to_gcs(source_file_path, bucket_name, object_key, project=GCP_PROJECT_NAME, credentials_file_path=GCP_CREDENTIALS_FILE):
    """Uploads a file to Google Cloud Storage.
    
    Parameters
    ----------
    source_file_path : str
        The local path to the file you want to upload.
        
    bucket_name : str
        The name of the Google Cloud Storage bucket.
    
    object_key : str
        The name to give to the object in Google Cloud Storage.
        
    project : str
        The name of the GCP project where the bucket exists.
        
    credentials_file_path : str
        The local path to the JSON credentials file for the GCP project.

    Returns
    -------
    url : str
        The URL of the uploaded object on Google Cloud Storage.
        
    """
    
    # Initialize the Google Cloud Storage client
    storage_client = storage.Client.from_service_account_json(credentials_file_path, project=project)

    # Get the bucket object
    bucket = storage_client.get_bucket(bucket_name)

    # Create a blob object representing the uploaded file
    blob = bucket.blob(object_key)

    # Upload the file
    blob.upload_from_filename(source_file_path)

    # Generate the URL for the uploaded object
    url = f"https://storage.googleapis.com/{bucket_name}/{object_key}"

    return url
    
    
def delete_object(bucket_name, object_key, project=GCP_PROJECT_NAME, credentials_file_path=GCP_CREDENTIALS_FILE):
    """Deletes an object in Google Cloud Storage.
    
    Parameters
    ----------
    bucket_name : str
        The name of the Google Cloud Storage bucket.
    
    object_key : str
        The name of the object to be deleted.
        
    project : str
        The name of the GCP project where the bucket exists.
        
    credentials_file_path : str
        The local path to the JSON credentials file for the GCP project.

    Returns
    -------
    None
        
    """
    
    # Initialize the Google Cloud Storage client
    storage_client = storage.Client.from_service_account_json(credentials_file_path, project=project)

    # Get the bucket object
    bucket = storage_client.get_bucket(bucket_name)

    # Get the file object
    blob = bucket.blob(object_key)

    # Delete the object
    try:
        blob.delete()
        
    except Exception as e:
        pass
