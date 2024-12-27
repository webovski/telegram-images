import os

def count_files_in_directory(directory_path):
    try:
        # List all entries in the directory
        entries = os.listdir(directory_path)
        # Filter out only files
        files = [entry for entry in entries if os.path.isfile(os.path.join(directory_path, entry))]
        return len(files)
    except FileNotFoundError:
        print(f"Directory not found: {directory_path}")
        return 0
    except PermissionError:
        print(f"Permission denied: {directory_path}")
        return 0

# Replace with your directory path
directory = 'all'
print(f"Number of files in '{directory}': {count_files_in_directory(directory)}")
