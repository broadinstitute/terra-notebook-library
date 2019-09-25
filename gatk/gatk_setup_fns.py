""" setup files for GATKTutorials-Germline notebooks

notes to future selves: 
- variables defined in Python that get pushed to the value stack become 
accessible to Bash using Jupyter Magics.
- to give Jupyter access to "global" variables such as BUCKET, we define them 
here outside of functions, but we need to import * in Jupyter to have them be 
pushed to the value stack.
- a global variable defined inside functions will not be pushed to the value stack

to do: 
- figure out how to push a global variable to the value stack without import *
- make use of decorators, if needed, to make sure if someone runs import gatk_init,
the globals do get pushed.

"""
import os
import pip


# Set your workspace bucket variable for this notebook.
BUCKET = os.environ['WORKSPACE_BUCKET']

# Set workshop variable to access the most recent materials
WORKSHOP = "workshop_1908"

# Set up directories for the files to live inside this notebook
file_directories = {'germline': ["/home/jupyter-user/2-germline-vd/sandbox/",
                                "/home/jupyter-user/2-germline-vd/ref",
                                "/home/jupyter-user/2-germline-vd/resources",
                                "/home/jupyter-user/2-germline-vd/gvcfs",
                                "/home/jupyter-user/CNN/Output/"],
                'somatic': ["/home/jupyter-user/sandbox"]
                }

# Set up command to check for data accessibility
check_data_commands = {'germline': 'gsutil ls gs://gatk-tutorials/'+WORKSHOP+'/2-germline/',
                        'somatic': 'gsutil ls gs://gatk-tutorials/'+WORKSHOP+'/3-somatic/'
                        }

# Set up commands to copy data to the notebook
data_copy_commands = {'germline': [ "gsutil cp gs://gatk-tutorials/"+WORKSHOP+"/2-germline/ref/* /home/jupyter-user/2-germline-vd/ref",
                                    "gsutil cp gs://gatk-tutorials/"+WORKSHOP+"/2-germline/trio.ped /home/jupyter-user/2-germline-vd/",
                                    "gsutil cp gs://gatk-tutorials/"+WORKSHOP+"/2-germline/resources/* /home/jupyter-user/2-germline-vd/resources/",
                                    "gsutil cp gs://gatk-tutorials/"+WORKSHOP+"/2-germline/gvcfs/* /home/jupyter-user/2-germline-vd/gvcfs/"],
                    'somatic': ["gsutil -m cp -r gs://gatk-tutorials/"+WORKSHOP+"/3-somatic/bams /home/jupyter-user/",
                                "gsutil -m cp -r gs://gatk-tutorials/"+WORKSHOP+"/3-somatic/ref /home/jupyter-user/",
                                "gsutil -m cp -r gs://gatk-tutorials/"+WORKSHOP+"/3-somatic/resources /home/jupyter-user/",
                                "gsutil -m cp -r gs://gatk-tutorials/"+WORKSHOP+"/3-somatic/mutect2_precomputed /home/jupyter-user/"]
                    }


def check_files(system_command, verbose=False):
    
    file_contents = os.popen(system_command).read()
    
    # parse a list of the accessible files
    accessible_files = []
    for f in file_contents.split('\n'):
        if 'gs://' in f:
            accessible_files.append(f)
    
    if len(accessible_files) > 0:
        outcome = 'Data is accessible!'
    else:
        outcome = 'WARNING: No data is accessible!'

    if verbose:
        print("\n\nAccessible files:")
        print('\t'+'\n\t'.join(accessible_files))
    else:
        print(outcome)

    return accessible_files

def gatk_init(tutorial, verbose=False):
    ''' tutorial = 'germline' or 'somatic'
    '''
    global BUCKET
    global WORKSHOP
    
    # Create directories for your files to live inside this notebook
    dirs_to_create = file_directories[tutorial]

    for path in dirs_to_create:
        if not os.path.exists(path):
            os.makedirs(path)

    # Check if data is accessible. The command should list several gs:// URLs.
    system_command = check_data_commands[tutorial]
    accessible_files = check_files(system_command, verbose)
    
    # if files were not listed, pip install google cloud
    # TODO: test that this works!
    if len(accessible_files) == 0:
        print('WARNING: no files were found. pip installing google-cloud-storage...')
        pip.main(['install', google-cloud-storage])

        # try again to access the files
        accessible_files = check_files(system_command, verbose)
        
        if len(accessible_files) == 0: # if you still have a problem
            print('WARNING: pip install google-cloud-storage did not solve the problem! Data not accessible.')


    # Download Data to the Notebook
    system_commands = data_copy_commands[tutorial]

    for system_command in system_commands:
        os.system(system_command)
        target_folder = system_command.split(" ")[-1]
        copied_files = os.popen("ls "+target_folder).read()
        if len(copied_files) > 0:
            outcome = 'Data copied successfully!'
        else:
            outcome = 'WARNING: No data copied!'
        if verbose:
            print("Copied files to "+target_folder+":")
            print(copied_files)
        else:
            print("Copied files to " + target_folder + " - " + outcome)


