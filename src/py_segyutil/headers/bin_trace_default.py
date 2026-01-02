def binary_trace_header_parameters():
        
    '''
    Create a python dictionary to read 400 byte binary trace header.
    Key = category as text line
    Dict[0] = first byte to read
    Dict[1] = end byte to read
    For each dictionary straing key, read from start  byte [key][0] to end byte dict[key][1] and store result in dict[key][2]
    For display purposes the start byte has +1 added
    Example:
    self.bin_dict = { "Job Identification Number":  [0, 4,0]} read bytes 0-4, format of python slicing is bytes 0-3. 
    For display, bytes are printed as 1 to 4, 5 to 8, 9 to ...etc etc
    KJAGGS FEB 2022
    '''
       
    bin_trace_dict = { "Job Identification Number":  [0, 4,0],
            "Line Number":  [4, 8,0],
            "Reel Number":  [8, 12,0],  
            "No. Data Traces Per Ensemble":  [12, 14,0],     
            "No. Auxillary Traces Per Ensemble":  [14, 16,0], 
            "Sample Interval In Microseconds":  [16, 18,0],   
            "Sample Interval In Microseconds Original Recording":  [18, 20,0],     
            "Number Samples Per Data Trace":  [20, 22,0],  
            "Number Samples Per Data Trace Original Recording":  [22, 24,0],    
            "Data Sample Format Code":  [24, 26,0], 
            "Ensemble Fold":  [26, 28,0],   
            "Trace Sorting Code":  [28, 30,0],  
            "Vertical Sum Code":  [30, 32,0],  
            "Sweep Frequency At Start":  [32, 34,0],     
            "Sweep Frequency At End":  [34, 36,0],  
            "Sweep Length ms":  [36, 38,0], 
            "Sweep Type Code":  [38, 40,0],     
            "Trace Number Of Sweep Channel":  [40, 42,0], 
            "Sweep Taper Length At Start milliseconds":  [42, 44,0], 
            "Sweep Taper Length At End milliseconds":  [44, 46,0], 
            "Taper Type":  [46, 48,0], 
            "Correlated Data Traces":  [48, 50,0],    
            "Binary Gain Recovered":  [50, 52,0], 
            "Amplitude Recovery Method":  [52, 54,0], 
            "Measurement System":  [54, 56,0], 
            "Impulse Signal Polarity":  [56, 58,0], 
            "Vibrator Polarity Code":  [58, 60,0], 
            "Unassigned":  [60, 100,0], 
            "SEGY Revision Format Number":  [100, 102,0],  
            "Fixed Trace Length Flag":  [102, 104,0],
            "Number Of Extended Textual Records":  [104, 106,0],  
            "Unassigned2":  [106, 200,0],            
            
        } #end of dictionary  

    return bin_trace_dict 