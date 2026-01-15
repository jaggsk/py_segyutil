import numpy as np

def create_trace_locations(expected_no_traces=None,no_bytes_trace_package=None,no_bytes_trace_header=None, ebcdic_bytes = 3600):

    '''
    Create numpy array denoting the following in columns
    1) Trace Number
    2) Start Trace Header Byte
    3) End Trace Header trace 
    4) Start Data Byte
    5) End Data Byte
    '''

    trace_no = np.arange(0, expected_no_traces, 1)

    arr = np.column_stack([
        trace_no,
        trace_no*no_bytes_trace_package + ebcdic_bytes,
        trace_no*no_bytes_trace_package + ebcdic_bytes + no_bytes_trace_header - 1,
        trace_no*no_bytes_trace_package + ebcdic_bytes + no_bytes_trace_header,
        trace_no*no_bytes_trace_package + ebcdic_bytes + no_bytes_trace_package - 1        

    ])
    
    return arr