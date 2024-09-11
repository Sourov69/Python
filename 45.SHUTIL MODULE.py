# The 'shutil' module in Python is a utility module that offers a high-level interface for file operations. It provides functions for copying, moving, archiving, and managing files and directories. This module enables you to perform tasks like copying files, copying directory trees, deleting files, and more, making file management and manipulation more convenient in Pytho

import shutil

# copying a file.. 
shutil.copy("main.py", "main2.py")

# removing file
import os
os.remove("main2.py")

# moving file
shutil.move("New folder/file1", "fileup")

# copying a folder..
shutil.copytree("New folder", "copytree folder")

# removing folder..
shutil.rmtree("copytree folder") 
