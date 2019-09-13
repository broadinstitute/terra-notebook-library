""" setup files for GATKTutorials-Germline notebooks
"""
import os

def gatk_setup():
    # Set your workspace bucket variable for this notebook.
    BUCKET = os.environ['WORKSPACE_BUCKET']

    return BUCKET
