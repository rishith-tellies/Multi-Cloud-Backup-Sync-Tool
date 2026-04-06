from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials

def get_drive_service():
    creds = Credentials.from_authorized_user_file('token.json')
    return build('drive', 'v3', credentials=creds)

def upload_to_drive(file_path, filename):
    print(f"Uploading to Drive: {filename}")

    service = get_drive_service()

    folder_id = "your-folder-id"  # Replace with your folder ID

    file_metadata = {
        'name': filename,
        'parents': [folder_id]   
    }

    media = MediaFileUpload(file_path)

    service.files().create(
        body=file_metadata,
        media_body=media
    ).execute()