import os
import sys

def segy_dir_check(in_segy_dir = None):
    '''
    Check if the user submitted directory is valid 
    TO DO - add error logging functionality 
    '''
    if os.path.isdir(in_segy_dir) == False:
        print(f"Directory {in_segy_dir} does not exist!")
        sys.exit()
    else:
        print(f"Valid file directory")
    
def segy_file_check(in_segy_file=None):
    '''
    Check if the user submitted filename is valid 
    TO DO - add error logging functionality 
    '''
    if os.path.isfile(in_segy_file) == False:
        print(f"File {in_segy_file} does not exist!")
        sys.exit()
    else:
        print(f"Valid file name")

def segy_file_valid(qc_path = None):


    #directory and file name information
    
    segy_dir, segy_file = os.path.split(qc_path)
    segy_dir_check(in_segy_dir = segy_dir)
    segy_file_check(in_segy_file = qc_path)

    return segy_dir, segy_file, os.path.getsize(qc_path)