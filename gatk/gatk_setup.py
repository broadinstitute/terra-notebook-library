""" setup files for GATKTutorials-Germline notebooks
"""

# Set your workspace bucket variable for this notebook.
import os
BUCKET = os.environ['WORKSPACE_BUCKET']

# Set workshop variable to access the most recent materials
WORKSHOP = "workshop_1908"

# Create directories for your files to live inside this notebook
! mkdir -p /home/jupyter-user/2-germline-vd/sandbox/
! mkdir -p /home/jupyter-user/2-germline-vd/ref
! mkdir -p /home/jupyter-user/2-germline-vd/resources
! mkdir -p /home/jupyter-user/2-germline-vd/gvcfs
! mkdir -p /home/jupyter-user/CNN/Output/
