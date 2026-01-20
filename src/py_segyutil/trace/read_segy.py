
from ..headers import read_single_trace_header
import pandas as pd

def read_segy_file_headers(segy_read_infile:str=None, trace_locations=None,trace_header_read_dict=None, byte_order = 'big'):

    with open(segy_read_infile,'rb') as filereader:

        trace_header_list = []

        for j in range(trace_locations.shape[0]):

            filereader.seek(trace_locations[j][1])
            trace_header_temp = filereader.read((trace_locations[j][2]-trace_locations[j][1])+1)
            trace_header_dict_temp = read_single_trace_header(trace_header_package=trace_header_temp,trace_header_loc_dict=trace_header_read_dict,trace_read_byte_order=byte_order)
            trace_header_list.append(trace_header_dict_temp)
            
        filereader.close()

    return pd.DataFrame(trace_header_list)