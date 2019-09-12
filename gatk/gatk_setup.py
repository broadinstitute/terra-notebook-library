""" setup files for GATKTutorials-Germline notebooks
"""

# Set your workspace bucket variable for this notebook.
import os
BUCKET = os.environ['WORKSPACE_BUCKET']

# Set workshop variable to access the most recent materials
WORKSHOP = "workshop_1908"

# Create directories for your files to live inside this notebook
dirs_to_create = ["/home/jupyter-user/2-germline-vd/sandbox/",
                  "/home/jupyter-user/2-germline-vd/ref",
                  "/home/jupyter-user/2-germline-vd/resources",
                  "/home/jupyter-user/2-germline-vd/gvcfs",
                  "/home/jupyter-user/CNN/Output/"]

for path in dirs_to_create:
  if not os.path.exists(path):
    os.makedirs(path)

# Check if data is accessible. The command should list several gs:// URLs.
system_command = "gsutil ls gs://gatk-tutorials/"+WORKSHOP+"/2-germline/"
file_contents = os.popen(system_command).read()
print("\n\nChecking if data is accessible. The command should list several gs:// URLS:")
for f in file_contents.split('\n'):
    print(f)
