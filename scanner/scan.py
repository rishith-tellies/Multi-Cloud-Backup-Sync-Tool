import os

def scan_directory(folder_path):
    file_list = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            full_path = os.path.join(root, file)

            file_list.append({
                "name": file,
                "path": full_path
            })

    return file_list