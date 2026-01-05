from .bin_trace_default import binary_trace_header_parameters

def segy_read_binary_header(binary_bin=None,big_endian = True): 
    '''
    Extract key parameters from binary trace header by iterating through dictionary.
    trace format code used to define the data format, bytes per sample and associated decoding parameters
    bytes per sample, samples per trace used to calculate number of bytes per data trace and also including trace header
    self.segy_integrity() used to sense check number of expected traces and confirm no unaccounted for bytes exist 
    KJAGGS FEB 2022
    '''
        
    bin_dict = binary_trace_header_parameters()
        
    if big_endian == True:
        #default for data decoding is big endian, adjusting to False will utilise Little Endian Format
        big_endian_def = 'big'   
    else:
        big_endian_def = 'little'   
        
        
    #iterate through each dictionary key and store the extracted integer from binary at position number 3 in the dictionary structure.
    for key in bin_dict:
        #print(bin_dict[key][0])
        bin_dict[key][2] = int.from_bytes(binary_bin[bin_dict[key][0]:bin_dict[key][1]], byteorder=big_endian_def)
    #        if self.print_summary == True:
    #            #binary trace header summary if requested
    #            print('{0}, bytes {1} to {2} = {3}'.format(key,self.bin_dict[key][0] + 1,self.bin_dict[key][1],self.bin_dict[key][2]))
        
        
    #assign key variables from binary trace header information
    #used to calculate expected number of traces, identify byte ranges for read trace headers, trace data etc
    #self.samples_per_trace = self.bin_dict["Number Samples Per Data Trace"][2]
    #sample rate in microseconds
    #self.sample_rate = self.bin_dict["Sample Interval In Microseconds"][2]
    #will be used to identify decode binary to float and calculate number of bytes per trace
    #self.trace_format_code = self.bin_dict["Data Sample Format Code"][2]
    #each integer value represents an extra 3200 byte data header following binary tarce header
    #self.textual_header_code = self.bin_dict["Number Of Extended Textual Records"][2]
        
        #
    #self.no_bytes_per_sample, self.data_format_code_text = self.sample_format_code()
    #print(self.no_bytes_per_sample, self.data_format_code_text)
        
    #number of bytes to read for seismic data portion of a trace ONLY
    #self.number_bytes_per_trace_data = self.samples_per_trace * self.no_bytes_per_sample
    #number of bytes to read for header and seismic data per trace
    #self.number_bytes_per_trace_package = self.number_bytes_per_trace_data + self.bytes_trace_header
        
    #calculate expected number of traces based upon calculated bytes per trace package and total header bytes
    #segy_integity() 
        
    #if self.print_summary == True:
    #    print("\n")
    #    print('Total number bytes input file = {0}'.format(self.input_file_size_bytes))
    #    print('Number of samples per trace = {0}'.format(self.samples_per_trace))
    #    print('Number of bytes per sample = {0}'.format(self.no_bytes_per_sample))
    #    print('Data format = {0}'.format(self.data_format_code_text))
    #    print('Number of bytes per trace data = {0}'.format(self.number_bytes_per_trace_data))
    #    print('Number of bytes per trace data incl. header = {0}'.format(self.number_bytes_per_trace_package )) 
    #    print('Number of expected textual header files = {0}'.format(self.textual_header_code)) 
    #    print('\nExpected number of seismic traces = {0}'.format(self.expected_number_of_traces)) 
    
        #print EBCDIC header to console
    #    self.segy_read_print_ebcdic()

    return bin_dict