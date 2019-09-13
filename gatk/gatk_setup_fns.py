""" setup files for GATKTutorials-Germline notebooks
"""
import os

def gatk_setup_1(verbose=False):
    # Set your workspace bucket variable for this notebook.
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
    if verbose:
        print("\n\nChecking if data is accessible. This should list several gs:// URLS:")
        for f in file_contents.split('\n'):
            print(f)

    # Download Data to the Notebook
    system_commands = ["gsutil cp gs://gatk-tutorials/"+WORKSHOP+"/2-germline/ref/* /home/jupyter-user/2-germline-vd/ref",
                    "gsutil cp gs://gatk-tutorials/"+WORKSHOP+"/2-germline/trio.ped /home/jupyter-user/2-germline-vd/",
                    "gsutil cp gs://gatk-tutorials/"+WORKSHOP+"/2-germline/resources/* /home/jupyter-user/2-germline-vd/resources/",
                    "gsutil cp gs://gatk-tutorials/"+WORKSHOP+"/2-germline/gvcfs/* /home/jupyter-user/2-germline-vd/gvcfs/"]

    for system_command in system_commands:
        os.system(system_command)
        target_folder = system_command.split(" ")[-1]
        copied_files = os.popen("ls "+target_folder).read()
        if verbose:
            print("Copied files to "+target_folder+":")
            print(copied_files)
    
    return BUCKET
