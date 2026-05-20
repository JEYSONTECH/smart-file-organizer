import os
import shutil

# Folder to organize
path = input("Enter folder path: ")

# File type folders
folders = {
    "Images": [".png", ".jpg", ".jpeg", ".gif"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Music": [".mp3", ".wav"]
}

# Create folders if they don't exist
for folder in folders:
    folder_path = os.path.join(path, folder)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Organize files
for file in os.listdir(path):

    file_path = os.path.join(path, file)

    if os.path.isfile(file_path):

        for folder, extensions in folders.items():

            for ext in extensions:

                if file.lower().endswith(ext):

                    destination = os.path.join(path, folder, file)

                    shutil.move(file_path, destination)

                    print(f"Moved: {file} -> {folder}")

print("Organization Complete.")
