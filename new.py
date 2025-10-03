import os

# Update these variables before running
REPO_DIR = '/path/to/your/local/repo'
FILE_TO_ADD = 'file_you_want_to_upload.txt'
COMMIT_MESSAGE = 'Add file via script'

# Change to the repository directory
os.chdir(REPO_DIR)

# Add the new/changed file to git
os.system(f'git add {FILE_TO_ADD}')

# Commit the file
os.system(f'git commit -m "{COMMIT_MESSAGE}"')

# Push to GitHub (main branch; use 'master' if your repo uses it)
os.system('git push origin main')
