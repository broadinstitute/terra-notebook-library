""" setup files for GATKTutorials-Germline notebooks
"""

def gatk_setup():
    # Set your workspace bucket variable for this notebook.
    import os
    BUCKET = os.environ['WORKSPACE_BUCKET']