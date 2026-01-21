def print_segy_summary(segy_summary_dict=None):

    '''
    Print parameters obtained from initial segy file loading
    '''
    print("\n")
    print('Segy file name = {0}'.format(segy_summary_dict['Input File Name']))
    print('Total number bytes input file = {0}'.format(segy_summary_dict['Input File Size Bytes']))
    print('Sample rate = {0}'.format(segy_summary_dict['Sample Rate']))
    print('Number of samples per trace = {0}'.format(segy_summary_dict['Number Samples Per Trace']))
    print('Number of bytes per sample = {0}'.format(segy_summary_dict['Number Bytes Per Sample']))
    print('Data type = {0}'.format(segy_summary_dict['Data Type']))
    print('Fold = {0}'.format(segy_summary_dict['Fold']))
    print('Trace format = {0}'.format(segy_summary_dict['Trace Format']))
    print('Number of bytes per trace data = {0}'.format(segy_summary_dict['Number Bytes Trace Data']))
    print('Number of bytes per trace ensemble incl. header = {0}'.format(segy_summary_dict['Number Bytes Trace Package'])) 
    print('Number of expected textual header files = {0}'.format(segy_summary_dict['Number Extended Textual Records'])) 
    print('\nExpected number of seismic traces = {0}'.format(segy_summary_dict['Expected Number Seismic Traces'])) 

