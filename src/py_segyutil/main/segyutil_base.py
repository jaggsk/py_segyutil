import os
from ..utils.file_check import segy_file_valid
from ..utils import sample_format_code, create_trace_locations, print_segy_summary
from ..headers import segy_read_ebcdic_header
from ..headers import segy_read_binary_header
from ..headers import data_trace_header_parameters
from ..trace.read_segy import read_segy_file_headers
#from ..trace import byte_adjustment

class SegyUtil:
    """
    Example class that runs the main functionality.
    """

    def __init__(self,
                 no_bytes_ebdcdic = 3200,no_bytes_bin_trace_header = 400,
                 no_bytes_trace_header = 240,no_bytes_extended_textual_header = 3200,
                 big_endian = True,) -> None:
        
        #standard byte length of the key information header - DO NOT CHANGE!!!!!
        self.no_bytes_ebcdic = no_bytes_ebdcdic 
        self.no_bytes_bin_trace_header = no_bytes_bin_trace_header
        self.no_bytes_trace_header = no_bytes_trace_header
        self.no_bytes_extended_textual_header = no_bytes_extended_textual_header
        
        #big endian set to true for decoding header information - default = 'big'
        if big_endian == True:
            self.big_endian = 'big'
        else:
            self.big_endian = 'little'

        self.segy_load_flag = 0



    def read_segy(self,segy_infile_read = None):

        #Host for downloaded parameters
        self.segy_params_dict = {}

        #Routine to file path string validity + check file size vs calculated structure
        self.segy_infile_read = segy_infile_read
        self.segy_infile_read_path, self.segy_infile_read_filename,self.segy_infile_read_size = segy_file_valid(qc_path= self.segy_infile_read)
        self.segy_params_dict['Input File String'] = self.segy_infile_read
        self.segy_params_dict['Input File Path'],self.segy_params_dict['Input File Name'],self.segy_params_dict['Input File Size Bytes'] = segy_file_valid(qc_path= self.segy_infile_read)

        #extract ebcdic and binary header byte portions and decode
        with open(self.segy_infile_read,'rb') as self.segy_infile_reader_binary:
            #read the required number of bytes for ebcdic header - standard = 3200 - decode to ascii
            self.segy_infile_read_ebcdic = segy_read_ebcdic_header(self.segy_infile_reader_binary.read(self.no_bytes_ebcdic))
            #read the required number of bytes for ebcdic header - standard = 400 = decode to integer
            self.segy_infile_read_binary = segy_read_binary_header(binary_bin=self.segy_infile_reader_binary.read(self.no_bytes_bin_trace_header),big_endian=self.big_endian)

            self.segy_infile_reader_binary.close()

        self.segy_params_dict['Number Bytes EBCDIC'] = self.no_bytes_ebcdic
        self.segy_params_dict['Number Bytes Binary Header'] = self.no_bytes_bin_trace_header
        self.segy_params_dict['Number Bytes Trace Header'] = self.no_bytes_trace_header
        self.segy_params_dict['Number Bytes Extended Textual Header'] = self.no_bytes_extended_textual_header
        self.segy_params_dict['SEGY Revision Format Number'] = self.segy_infile_read_binary['SEGY Revision Format Number'][2]
        self.segy_params_dict['Fold'] = self.segy_infile_read_binary['Ensemble Fold'][2]


        self.segy_params_dict['Number Extended Textual Records'] = self.segy_infile_read_binary['Number Of Extended Textual Records'][2] 

        self.segy_params_dict['Number Bytes Per Sample'],self.segy_params_dict['Trace Format'] = sample_format_code(trace_format_code=self.segy_infile_read_binary['Data Sample Format Code'][2])
        self.segy_params_dict['Trace Format Code'] = self.segy_infile_read_binary['Data Sample Format Code'][2]
        
        self.segy_params_dict['Data Type'] = None

        if self.segy_infile_read_binary['Sample Interval In Microseconds'][2] == 1:
            self.segy_params_dict['Data Type'] = "Stack"
        else:
            self.segy_params_dict['Data Type'] = "Gather"            
        
        self.segy_params_dict['Number Samples Per Trace'] = self.segy_infile_read_binary['Number Samples Per Data Trace'][2]

        self.segy_params_dict['Number Bytes Header Package'] = self.segy_params_dict['Number Bytes EBCDIC'] + self.segy_params_dict['Number Bytes Binary Header'] + (self.segy_params_dict['Number Extended Textual Records'] * self.segy_params_dict['Number Bytes Extended Textual Header'])
        self.segy_params_dict['Number Bytes Trace Data'] = self.segy_params_dict['Number Samples Per Trace'] * self.segy_params_dict['Number Bytes Per Sample']
        self.segy_params_dict['Number Bytes Trace Package'] = self.segy_params_dict['Number Bytes Trace Header'] + self.segy_params_dict['Number Bytes Trace Data']
        self.segy_params_dict['Sample Rate'] = self.segy_infile_read_binary['Sample Interval In Microseconds'][2]

        if (self.segy_params_dict['Input File Size Bytes']-self.segy_params_dict['Number Bytes Header Package']) % self.segy_params_dict['Number Bytes Trace Package'] != 0:
            print("WARNING - expected number of traces is not an INTEGER - CHECK MANUALLY")
            # TO DO - Raise error module

        self.segy_params_dict['Expected Number Seismic Traces'] = int((self.segy_params_dict['Input File Size Bytes']-self.segy_params_dict['Number Bytes Header Package']) / self.segy_params_dict['Number Bytes Trace Package'])  

        #add standard trace header parameters to a dictionary within class
        self.trace_header_dict = data_trace_header_parameters()

        self.segy_load_flag = 1


    #def segy_trace_validation(self):

        #calculate header and databyte portions of input file
        #self.total_header_bytes = self.no_bytes_ebcdic + self.no_bytes_bin_trace_header + (self.segy_binary['Number Of Extended Textual Records'][2]*self.no_bytes_extended_textual_header)
        #self.total_data_bytes = self.segy_size - self.total_header_bytes

        #determine that number data trace bytes / bytes per package is an integer multiple, print warngin if not case
        #if self.total_data_bytes % self.no_bytes_per_trace_package != 0:
        #    print("WARNING - expected number of traces is not an INTEGER - CHECK MANUALLY")

        #calculate expected number of data traces within the file
        #self.expected_number_of_traces = int(self.total_data_bytes / self.no_bytes_per_trace_package)  


    def read_segy_summary(self):

        print_segy_summary(segy_summary_dict=self.segy_params_dict)

        #print("\n")
        #print('Total number bytes input file = {0}'.format(self.segy_size))
        #print('Sample Rate = {0}'.format(self.segy_binary['Sample Interval In Microseconds'][2]))
        #print('Number of samples per trace = {0}'.format(self.segy_binary['Number Samples Per Data Trace'][2]))
        #print('Number of bytes per sample = {0}'.format(self.number_bytes_per_sample))
        #print('Fold = {0}'.format(self.segy_binary['Ensemble Fold'][2]))
        #print('Data format = {0}'.format(self.trace_format_code_string))
        #print('Number of bytes per trace data = {0}'.format(self.number_bytes_per_trace_data))
        #print('Number of bytes per trace ensemble incl. header = {0}'.format(self.number_bytes_per_trace_package)) 
        #print('Number of expected textual header files = {0}'.format(self.segy_binary['Number Of Extended Textual Records'][2])) 
        #print('\nExpected number of seismic traces = {0}'.format(self.expected_number_of_traces)) 

    def read_all_headers(self, header_byte_dict=None):
        #self.trainer.trainer_test()

        df_header = read_segy_file_headers(segy_read_infile=self.segy_infile_read,trace_locations = self.segy_trace_locations,trace_header_read_dict=header_byte_dict,byte_order=self.big_endian)

        return df_header

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
