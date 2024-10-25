import os

# Specify the directory path (replace 'bikaladhikari' with your actual directory name)
directory = '/Users/bikaladhikari'  # This assumes 'bikaladhikari' is your username

# Get the list of files and directories in the specified directory
contents = os.listdir(directory)

# Print each item in the directory
for item in contents:
    print(item)

