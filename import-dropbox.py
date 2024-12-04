import dropbox
import os

# Initialize Dropbox client with your access token
ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN_HERE'
dbx = dropbox.Dropbox(ACCESS_TOKEN)

def download_file_from_dropbox(dropbox_path, local_path):
    """Download a file from Dropbox and save it to the local path."""
    try:
        metadata, response = dbx.files_download(path=dropbox_path)
        with open(local_path, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded {dropbox_path} to {local_path}")
    except Exception as e:
        print(f"Failed to download {dropbox_path}: {e}")

def download_all_files(folder_path, local_dir):
    """Download all files from the given Dropbox folder path to the local directory."""
    try:
        result = dbx.files_list_folder(folder_path)
        
        for entry in result.entries:
            if isinstance(entry, dropbox.files.FileMetadata):
                local_file_path = os.path.join(local_dir, entry.name)
                download_file_from_dropbox(entry.path_lower, local_file_path)
            elif isinstance(entry, dropbox.files.FolderMetadata):
                # Recursively download folder contents
                new_local_dir = os.path.join(local_dir, entry.name)
                os.makedirs(new_local_dir, exist_ok=True)
                download_all_files(entry.path_lower, new_local_dir)
                
        while result.has_more:
            result = dbx.files_list_folder_continue(result.cursor)
            for entry in result.entries:
                if isinstance(entry, dropbox.files.FileMetadata):
                    local_file_path = os.path.join(local_dir, entry.name)
                    download_file_from_dropbox(entry.path_lower, local_file_path)
                elif isinstance(entry, dropbox.files.FolderMetadata):
                    new_local_dir = os.path.join(local_dir, entry.name)
                    os.makedirs(new_local_dir, exist_ok=True)
                    download_all_files(entry.path_lower, new_local_dir)
                    
    except Exception as e:
        print(f"Failed to list or download files from {folder_path}: {e}")

def main():
    # Set your Dropbox folder path and local download directory
    dropbox_folder_path = ''
    local_directory = 'path_to_local_directory'
    
    os.makedirs(local_directory, exist_ok=True)
    download_all_files(dropbox_folder_path, local_directory)

if __name__ == "__main__":
    main()
