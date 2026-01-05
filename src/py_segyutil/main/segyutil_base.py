import os
from ..utils.file_check import segy_file_valid
from ..utils import sample_format_code, read_validation
from ..headers import segy_read_ebcdic_header
from ..headers import segy_read_binary_header

class SegyUtil:
    """
    Example class that runs the main functionality.
    """

    def __init__(self,
                 bytes_ebdcdic = 3200,bytes_bin_trace_header = 400,
                 bytes_trace_header = 240,bytes_extended_textual_header = 3200,
                 big_endian = True,) -> None:
        
        #standard byte length of the key information header - DO NOT CHANGE!!!!!
        self.bytes_ebcdic = bytes_ebdcdic 
        self.bytes_bin_trace_header = bytes_bin_trace_header
        self.bytes_trace_header = bytes_trace_header
        self.bytes_extended_textual_header = bytes_extended_textual_header
        
        #big endian set to true for decoding header information - default = 'big'
        if big_endian == True:
            self.big_endian = 'big'
        else:
            self.big_endian = 'little'

        #assign all class variables to a dictionary - appears to dynamically update....
        self.segy_dict =  vars(self)


    def read_segy(self,segy_path = None):

        self.segy_infile_read = segy_path
        self.segy_path, self.segy_file,self.segy_size = segy_file_valid(qc_path= self.segy_infile_read)

        
        with open(self.segy_infile_read,'rb') as self.segy_infile_reader_binary:
            #read the required number of bytes for ebcdic header - standard = 3200
            self.segy_ebcdic = segy_read_ebcdic_header(self.segy_infile_reader_binary.read(self.bytes_ebcdic))
            #read the required number of bytes for ebcdic header - standard = 400
            self.segy_binary = segy_read_binary_header(binary_bin=self.segy_infile_reader_binary.read(self.bytes_bin_trace_header))

            self.segy_infile_reader_binary.close()


        self.trace_format_code,self.trace_format_code_string = sample_format_code(trace_format_code=self.segy_binary['Data Sample Format Code'][2])

        read_validation()

    def run(self) -> None:
        """Run the main logic"""
        print(f"✅ Hello {self.name}, class ran successfully!")