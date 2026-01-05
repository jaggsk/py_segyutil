import os
from ..utils.file_check import segy_file_valid
from ..headers import segy_read_ebcdic_header

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
            #self.ebcdic_bin = self.segy_infile_reader_binary.read(self.bytes_ebcdic)
            
            #read the required number of bytes for binary trace header - standard = 400
            #self.bin_trace_head_bin = self.segy_infile_reader_binary.read(self.bytes_bin_trace_header)

            #read 3200 byte EBCDIC and output entire text header to list
            #self.segy_read_ebcdic_header()
            
            #Extract key parameters from binary trace header by iterating through dictionary.
            #trace format code used to define the data format, bytes per sample and associated decoding parameters
            #use above info to calculate number of byte per trace and incl trace header
            #check number of traces present based upon file size in bytes, total initila header in bytes and bytes per trace package
            #if discrepancy in calculation issue warning
            #self.segy_read_binary_header()
            
            #if self.textual_header_code > 0:
            #    print("Number of extended textual headers found =", self.textual_header_code)
            #    self.extended_textual_head_bin = self.segy_infile_reader_binary.read((self.textual_header_code*self.bytes_extended_textual_header))
            #else:
            #    print("No extended textual header files found")           

            #close open read file
            self.segy_infile_reader_binary.close()

        print(self.segy_ebcdic)
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