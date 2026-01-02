def sample_format_code(trace_format_code :int = None):
        '''
        (int)->(int)(string)
        Routine to determine binary to floating point conversion format of SEGY data
        Outputs the number of bytes per sample and accompanying string descriptor
        Original code is extracted from the 400 byte SEG-Y binary header - bytes 3201- 3600
        Trace code is located at bytes 3223-3224
        Current standards are defined for integers 1-8
        Example: input code = 5, No of bytes/sample = 4 , output text = "4-byte IEEE floating-point"
        https://www.seg.org/Portals/0/SEG/News%20and%20Resources/Technical%20Standards/seg_y_rev1.pdf - Page 6
        KJAGGS FEB 2022
        '''
        #print(int_code_sample)

        int_no_bytes_sample = 0
        text_code_sample = "Unknown"
        if trace_format_code == 1:
            int_no_bytes_sample = 4 
            text_code_sample = "4-byte IBM floating-point" 
        elif trace_format_code == 2:
            int_no_bytes_sample = 4
            text_code_sample = "4-byte two's complement integer" 
        elif trace_format_code == 3:
            int_no_bytes_sample = 2
            text_code_sample = "2-byte two's complement integer" 
        elif trace_format_code == 4:
            int_no_bytes_sample = 4
            text_code_sample = "4-byte fixed-point with gain (obsolete)" 
        elif trace_format_code == 5:
            int_no_bytes_sample = 4
            text_code_sample = "4-byte IEEE floating-point" 
        elif trace_format_code == 6:
            int_no_bytes_sample = 0
            text_code_sample = "Not currently used" 
        elif trace_format_code == 7:
            int_no_bytes_sample = 0
            text_code_sample = "Not currently used"     
        elif trace_format_code == 8:
            int_no_bytes_sample = 1
            text_code_sample = "1-byte two's complement integer"  
        else:
            int_no_bytes_sample = 0
            text_code_sample = "Unknown"     
        
        return int_no_bytes_sample, text_code_sample