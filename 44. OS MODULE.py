# The os module in Python provides a way to interact with the operating system. It offers functions to perform operating system-dependent operations, such as working with files and directories, managing processes, and handling paths. The os module enables tasks like file manipulation, directory operations, environment variables access, and other system-level functionalities.
# # # #
import os
if (not os.path.exist("data")):
    os.mkdir("data")

for i in range(0, 100):
    os.mkdir(f'data/Day{i+1}')

# Renaming ---
import os
if os.mkdir(not os.path.exists("data")):
    os.mkdir("data")

for i in range(0, 100):
    os.rename(f"data/Day{i+1}", f"data/Tutorial{i+1}")

# oslist.py
import os
folders = os.listdir("data")
print(folders)

for folder in folders:
    print(folder)




import os

# Get the current working directory
current_directory = os.getcwd()
print("Current working directory:", current_directory)

# List the contents of a directory
directory_contents = os.listdir(current_directory)
print("Directory contents:", directory_contents)

# Create a new directory
new_directory = "new_folder"
os.mkdir(new_directory)
print(f"Created {new_directory} directory")

# Check if a path exists
path_exists = os.path.exists(new_directory)
print(f"{new_directory} exists:", path_exists)

# Remove the directory
os.rmdir(new_directory)
print(f"Removed {new_directory} directory")