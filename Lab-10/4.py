import os
import shutil

source_folder = "File_Handling"
file_name = "demo.csv"  # the file you want to copy
source_path = os.path.join(source_folder, file_name)

# Step 2: Create destination subdirectory
destination_folder = "Sub_directory"
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Step 3: Define destination file path
destination_path = os.path.join(destination_folder, file_name)

# Step 4: Copy the file
if os.path.isfile(source_path):
    shutil.copy(source_path, destination_path)
    print(f"File copied from '{source_path}' to '{destination_path}'")
else:
    print(f"Source file '{source_path}' does not exist.")
