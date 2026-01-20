from .bin_trace_default import binary_trace_header_parameters
from ..utils import byte_adjustment

def segy_read_binary_header(binary_bin=None,big_endian = None): 
    '''
    Extract key parameters from binary trace header by iterating through dictionary.
    trace format code used to define the data format, bytes per sample and associated decoding parameters
    bytes per sample, samples per trace used to calculate number of bytes per data trace and also including trace header
    self.segy_integrity() used to sense check number of expected traces and confirm no unaccounted for bytes exist 
    KJAGGS FEB 2022
    '''
        
    bin_dict = binary_trace_header_parameters()
        
    #iterate through each dictionary key and store the extracted integer from binary at position number 3 in the dictionary structure.
    for key in bin_dict:
        first_byte, byte_length = byte_adjustment(first_byte=bin_dict[key][0],last_byte=bin_dict[key][1])
        bin_dict[key][2] = int.from_bytes(binary_bin[first_byte:byte_length], byteorder=big_endian)

    return bin_dict