# Checking How many files and folders are there in a directory
import os

# Specify the path
PATH = "I:\Graphics"

files, dirs = 0, 0
for root, dirsname, filesname in os.walk(PATH):
    print("Looking in: ", root)
    files += len(filesname)
    dirs += len(dirsname)

print("Files: ", files)
print("Directories: ", dirs)
print("Total: ", files + dirs)