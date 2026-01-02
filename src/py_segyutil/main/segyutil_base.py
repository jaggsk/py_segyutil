import os
from ..utils.file_check import segy_file_valid

class SegyUtil:
    """
    Example class that runs the main functionality.
    """

    def __init__(self,
                 bytes_ebdcdic = 3200,bytes_bin_trace_header = 400,
                 bytes_trace_header = 240,bytes_extended_textual_header = 3200,
                 big_endian = True,) -> None:
        


        #assign all class variables to a dictionary - appears to dynamically update....
        self.segy_dict =  vars(self)


    def read_segy(self,segy_path = None):


        self.segy_infile_read = segy_path

        segy_file_valid(qc_path= self.segy_infile_read)
        #directory and file name information
        #self.cwd = os.getcwd() 

        #self.in_segy_dir, self.in_segy_file = os.path.split(self.segy_infile_read)
        
        #check if the user supplied directory is valid
        #self.segy_dir_check()
        ##check if the user supplied filename is valid
        #self.segy_file_check()

        #pass

    def run(self) -> None:
        """Run the main logic"""
        print(f"✅ Hello {self.name}, class ran successfully!")