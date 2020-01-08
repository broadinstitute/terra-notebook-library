# Set your workspace bucket variable for this notebook.
import os
BUCKET = os.environ['WORKSPACE_BUCKET']

# Set workshop variable to access the most recent materials
WORKSHOP = "workshop_1910"

# Create directories for your files to live inside this notebook
! mkdir -p /home/jupyter-user/2-germline-vd/sandbox/
! mkdir -p /home/jupyter-user/2-germline-vd/ref
! mkdir -p /home/jupyter-user/2-germline-vd/resources
! mkdir -p /home/jupyter-user/2-germline-vd/gvcfs
! mkdir -p /home/jupyter-user/CNN/Output/

# Check if data is accessible. The command should list several gs:// URLs.
! gsutil ls gs://gatk-tutorials/$WORKSHOP/2-germline/

##

# If you do not see gs:// URLs listed above, uncomment the last line in this cell
# and run it to install Google Cloud Storage. 
# Afterwards, restart the kernel with Kernel > Restart.
#! pip install google-cloud-storage

##

! gsutil cp gs://gatk-tutorials/$WORKSHOP/2-germline/ref/* /home/jupyter-user/2-germline-vd/ref
! gsutil cp gs://gatk-tutorials/$WORKSHOP/2-germline/trio.ped /home/jupyter-user/2-germline-vd/
! gsutil cp gs://gatk-tutorials/$WORKSHOP/2-germline/resources/* /home/jupyter-user/2-germline-vd/resources/
! gsutil cp gs://gatk-tutorials/$WORKSHOP/2-germline/gvcfs/* /home/jupyter-user/2-germline-vd/gvcfs/