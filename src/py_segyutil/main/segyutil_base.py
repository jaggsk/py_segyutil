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


        self.bytes_per_sample,self.trace_format_code_string = sample_format_code(trace_format_code=self.segy_binary['Data Sample Format Code'][2])

        self.number_bytes_per_trace_data = self.segy_binary['Number Samples Per Data Trace'][2] * self.number_bytes_per_trace_data
        self.number_bytes_per_trace_package = self.number_bytes_per_trace_data * self.segy_binary['No. Data Traces Per Ensemble'][2]

        #calculate header and databyte portions of input file
        self.total_header_traces = self.bytes_ebcdic + self.bytes_bin_trace_header + (self.segy_binary['Number Of Extended Textual Records'][2]*self.bytes_extended_textual_header)
        self.total_data_traces = self.segy_size - self.bytes_ebcdic - self.bytes_bin_trace_header - (self.textual_header_code*self.bytes_extended_textual_header)

        #determine that number data trace bytes / bytes per package is an integer multiple, print warngin if not case
        if self.total_data_traces % self.number_bytes_per_trace_package != 0:
            print("WARNING - expected number of traces is not an INTEGER - CHECK MANUALLY")

        #calculate expected number of data traces within the file
        self.expected_number_of_traces = int(self.total_data_traces / self.number_bytes_per_trace_package)  

    def read_segy_summary(self):

        print("\n")
        print('Total number bytes input file = {0}'.format(self.segy_size))
        print('Number of samples per trace = {0}'.format(self.segy_binary['Number Samples Per Data Trace'][2]))
        print('Number of bytes per sample = {0}'.format(self.bytes_per_sample))
        print('Data format = {0}'.format(self.trace_format_code_string))
        print('Number of bytes per trace data = {0}'.format(self.number_bytes_per_trace_data))
        print('Number of bytes per ensemble = {0}'.format(self.number_bytes_per_trace_package))
        print('Number of bytes per trace ensemble incl. header = {0}'.format(self.number_bytes_per_trace_package +self.bytes_trace_header)) 
        print('Number of expected textual header files = {0}'.format(self.segy_binary['Number Of Extended Textual Records'][2])) 
        print('\nExpected number of seismic traces = {0}'.format(self.expected_number_of_traces)) 







    def run(self) -> None:
        """Run the main logic"""
        print(f"✅ Hello {self.name}, class ran successfully!")