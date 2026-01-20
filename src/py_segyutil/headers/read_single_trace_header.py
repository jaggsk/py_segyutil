from ..utils import byte_adjustment

def read_single_trace_header(trace_header_package = None,trace_header_loc_dict=None, trace_read_byte_order = 'big'):

    '''
    Function to decode supplied byte positions from trace header file
    
    trace_header_package: Default = None. 240 bytes containing trace header information
    trace_header_loc_dict:Default = None - supplied dictionary - key = paramater value = list of two integers, start and end byte
    trace_read_byte+order: Default = big - big endian byte order, alternative = little 
    
    Returns a dictionary with same keys but decoded bytes as values

    K Jaggs Jan 2026
    '''

    read_trace_header_dict = {}

    for key, value in trace_header_loc_dict.items():

        first_byte, byte_length = byte_adjustment(first_byte= value[0],last_byte = value[1])
        read_trace_header_dict[key]  = int.from_bytes(trace_header_package[first_byte:byte_length], byteorder=trace_read_byte_order , signed=True)

    return read_trace_header_dict