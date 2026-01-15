import os
from ..utils.file_check import segy_file_valid
from ..utils import sample_format_code, create_trace_locations
from ..headers import segy_read_ebcdic_header
from ..headers import segy_read_binary_header
from ..headers import data_trace_header_parameters

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


        self.trainer = Trainer(self)
        #assign all class variables to a dictionary - appears to dynamically update....
        #self.segy_dict =  vars(self)


    def read_segy(self,segy_path = None):

        self.segy_infile_read = segy_path
        self.segy_path, self.segy_file,self.segy_size = segy_file_valid(qc_path= self.segy_infile_read)

        
        with open(self.segy_infile_read,'rb') as self.segy_infile_reader_binary:
            #read the required number of bytes for ebcdic header - standard = 3200
            self.segy_ebcdic = segy_read_ebcdic_header(self.segy_infile_reader_binary.read(self.bytes_ebcdic))
            #read the required number of bytes for ebcdic header - standard = 400
            self.segy_binary = segy_read_binary_header(binary_bin=self.segy_infile_reader_binary.read(self.bytes_bin_trace_header))

            self.segy_infile_reader_binary.close()

        self.number_bytes_per_sample,self.trace_format_code_string = sample_format_code(trace_format_code=self.segy_binary['Data Sample Format Code'][2])

        if self.segy_binary['Sample Interval In Microseconds'][2] == 1:
            self.data_type = "Stack"
        else:
            self.data_type = "Gather"            

        self.number_bytes_per_trace_data = self.segy_binary['Number Samples Per Data Trace'][2] * self.number_bytes_per_sample
        self.number_bytes_per_trace_package = self.number_bytes_per_trace_data + self.bytes_trace_header
        self.sample_rate = self.segy_binary['Sample Interval In Microseconds'][2]

        self.trace_header_dict = data_trace_header_parameters()

        self.segy_trace_validation()

        self.segy_trace_locations = create_trace_locations(expected_no_traces=self.expected_number_of_traces,no_bytes_trace_package=self.number_bytes_per_trace_package,no_bytes_trace_header=self.bytes_trace_header,ebcdic_bytes=self.bytes_ebcdic)

    def segy_trace_validation(self):

        #calculate header and databyte portions of input file
        self.total_header_bytes = self.bytes_ebcdic + self.bytes_bin_trace_header + (self.segy_binary['Number Of Extended Textual Records'][2]*self.bytes_extended_textual_header)
        self.total_data_bytes = self.segy_size - self.total_header_bytes

        #determine that number data trace bytes / bytes per package is an integer multiple, print warngin if not case
        if self.total_data_bytes % self.number_bytes_per_trace_package != 0:
            print("WARNING - expected number of traces is not an INTEGER - CHECK MANUALLY")

        #calculate expected number of data traces within the file
        self.expected_number_of_traces = int(self.total_data_bytes / self.number_bytes_per_trace_package)  

    def read_segy_summary(self):

        print("\n")
        print('Total number bytes input file = {0}'.format(self.segy_size))
        print('Sample Rate = {0}'.format(self.segy_binary['Sample Interval In Microseconds'][2]))
        print('Number of samples per trace = {0}'.format(self.segy_binary['Number Samples Per Data Trace'][2]))
        print('Number of bytes per sample = {0}'.format(self.number_bytes_per_sample))
        print('Fold = {0}'.format(self.segy_binary['Ensemble Fold'][2]))
        print('Data format = {0}'.format(self.trace_format_code_string))
        print('Number of bytes per trace data = {0}'.format(self.number_bytes_per_trace_data))
        print('Number of bytes per trace ensemble incl. header = {0}'.format(self.number_bytes_per_trace_package)) 
        print('Number of expected textual header files = {0}'.format(self.segy_binary['Number Of Extended Textual Records'][2])) 
        print('\nExpected number of seismic traces = {0}'.format(self.expected_number_of_traces)) 


    def read_all_headers(self):
        self.trainer.trainer_test()

    def read_trace(self):
        self.trainer.trainer_test()

    def update_header(self):
        self.trainer.trainer_test()

    def update_trace(self):
        self.trainer.trainer_test()

    def run(self) -> None:
        """Run the main logic"""
        print(f"✅ Hello {self.name}, class ran successfully!")




class Trainer:
    def __init__(self, segyutil_parent):
        self.segyutil_parent = segyutil_parent

    def trainer_test(self):

        print("It Worked!", self.segyutil_parent.segy_binary['Sample Interval In Microseconds'][2])
