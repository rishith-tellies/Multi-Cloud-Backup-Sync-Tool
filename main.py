from scanner.scan import scan_directory
from sync.engine import sync_files

if __name__ == "__main__":
    folder = input("Enter folder path: ")

    files = scan_directory(folder)

    print(f"Found {len(files)} files")

    sync_files(files)