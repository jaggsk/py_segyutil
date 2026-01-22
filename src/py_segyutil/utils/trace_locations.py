import numpy as np

def create_trace_locations(segy_param_dict=None):
#def create_trace_locations(expected_no_traces=None,no_bytes_trace_package=None,no_bytes_trace_header=None, ebcdic_bin_header_bytes = 3600):

    '''
    Create numpy array denoting the following in columns
    1) Trace Number
    2) Start Trace Header Byte
    3) End Trace Header trace 
    4) Start Data Byte
    5) End Data Byte

    Requires segy param dictionary loaded from segyutil_base.py

    PRECONDITION - SEGY data parameters are successfully retrieved
    '''

    trace_no = np.arange(0, segy_param_dict['Expected Number Seismic Traces'], 1)

    arr = np.column_stack([
        trace_no,
        trace_no*segy_param_dict['Number Bytes Trace Package'] + segy_param_dict['Number Bytes Header Package'],
        trace_no*segy_param_dict['Number Bytes Trace Package'] + segy_param_dict['Number Bytes Header Package'] + segy_param_dict['Number Bytes Trace Header'] - 1,
        trace_no*segy_param_dict['Number Bytes Trace Package'] + segy_param_dict['Number Bytes Header Package'] + segy_param_dict['Number Bytes Trace Header'],
        trace_no*segy_param_dict['Number Bytes Trace Package'] + segy_param_dict['Number Bytes Header Package'] + segy_param_dict['Number Bytes Trace Header'] - 1        

    ])
    
    return arr