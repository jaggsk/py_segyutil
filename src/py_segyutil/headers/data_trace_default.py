def data_trace_header_parameters():
        '''
        Create a python dictionary to read 240 byte trace header.
        Standard format as defined below
        https://www.seg.org/Portals/0/SEG/News%20and%20Resources/Technical%20Standards/seg_y_rev1.pdf
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
        
        trace_head_dict = { "Trace Sequence Number":  [0, 4,0],
                    "Trace Sequence Number within SEGY File":  [4, 8,0],
                    "Original Field Record Number":  [8, 12,0],  
                    "Trace Number Within Original Field Record":  [12, 16,0],     
                    
                    "Energy Source Point Number":  [16, 20,0], 
                    "Ensemble Number":  [20, 24,0],   
                    "Trace Number Within Ensemble":  [24, 28,0],     
                    "Trace Identification Code":  [28, 29,0],  
                    "Number Of Vertically Summed Traces":  [30, 32,0],    
                    "Number Of Horizontally Summed Traces":  [32, 34,0], 
                    "Data Use":  [34, 36,0],   
                    "Distance Centre Source Point To Centre Receiver Point":  [36, 40,0],  
                    
                    "Receiver Group Elevation":  [40, 44,0],  
                    "Source Group Elevation":  [44, 48,0],     
                    "Source Depth Below Surface":  [48, 52,0],  
                    "Datum Elevation  At Receiver Group":  [52, 56,0], 
                    "Datum Elevation  At Source":  [56, 60,0],     
                    "Water Depth At Source":  [60, 64,0], 
                    "Water Depth At Group":  [64, 68,0], 
                    "Elevation And Depth Scalar":  [68, 70,0], 
                    "Coordinate Scalar":  [70, 72,0], 
                    "Source X":  [72, 76,0], 
                    "Source Y":  [76, 80,0], 
                    "Group X":  [80, 84,0], 
                    "Group Y":  [84, 88,0],       
                    "Weathering Velocity":  [90, 92,0],    
                    "Subweathering Velocity":  [92, 94,0],    
                    "Uphole Time At Source":  [94, 96,0], 
                    "Uphole Time At Group":  [96, 98,0],      
                    
                    "Source Static Correction":  [98, 100,0], 
                    "Group Static Correction":  [100, 102,0], 
                    "Total Static":  [102, 104,0], 
                    "Lag Time A":  [104, 106,0],       
                    "Lag Time B":  [106, 108,0],    
                    "Delay Recoprding Time":  [108, 110,0],    
                    "Mute Time Start ":  [110, 112,0], 
                    "Mute Time End":  [112, 114,0],                   
                    "Number Samples In This Trace":  [114, 116,0],   
                    "Sample Interval Microseconds":  [116, 118,0],                    
         
                    "Gain Type Field Instruments":  [118, 120,0], 
                    "Instrument Gain Constant dB":  [120, 122,0], 
                    "Instrument Early Gain dB":  [122, 124,0], 
                    "Correlated":  [124, 126,0],       
                    "Sweep Frequency Start":  [126, 128,0],    
                    "Sweep Frequency End":  [128, 130,0],    
                    "Sweep Length Milliseconds ":  [130, 132,0], 
                    "Sweep Type":  [132, 134,0],                   
                    "Sweep Trace Taper Length Start":  [134, 136,0],  
                    "Sweep Trace Taper Length End":  [136, 138,0],  
                    "Taper Type":  [138, 140,0],   
                    
                    "Anti Alias Filter Freq (Hz) if used":  [140, 142,0], 
                    "Alias Filter Slope (dB/Octave)":  [142, 144,0], 
                    "Notch Filter Freq (Hz), if used":  [144, 146,0],   
                    "Notch Filter Slope (dB/Octave)":  [146, 148,0],
                    "Low Cut Freq (Hz), if used":  [148, 150,0],
                    "High Cut Freq (Hz), if used":  [150, 152,0],
                    "Low Cut Slope (dB/Octave)":  [152, 154,0],
                    "High Cut Slope (dB/Octave)":  [154, 156,0], 
                    "Year Data Recorded":  [156, 158,0],  

                    "Day Of Year":  [158, 160,0], 
                    "Hour Of Day":  [160, 162,0], 
                    "Minute Of Hour":  [162, 164,0],   
                    "Second Of Minute":  [164, 166,0],
                    "Time Basis Code":  [166, 168,0],
                    "Trace Weighting Factor":  [168, 170,0],
                    "Geophone Group Number Of Roll Switch Position One":  [170, 172,0],
                    "Geophone Group Number Of Trace Number One Within Original Field Record":  [172, 174,0], 
                    "Geophone Group Number Of Last Trace Within Original Field Record":  [174, 176,0],                        
                    "Gap Size":  [176, 178,0], 
                    "Over Travel Associated With Taper":  [178, 180,0], 
                    "X Coordinate CDP":  [180, 184,0],   
                    "Y Coordinate CDP":  [184, 188,0],
                    "3D Inline":  [188, 192,0],
                    "3D Xline":  [192, 196,0],
                    "Shotpoint Number 2D":  [196, 200,0],
                    
                    "Shotpoint Scalar":  [200, 202,0], 
                    "Trace Value Measurement Unit":  [202, 204,0],    
                    "Transduction Constant":  [204, 210,0], 
                    "Transduction Units":  [210, 212,0],  
                    "Device/Trace Identifier":  [212, 214,0],            

                    "TWT Scalar":  [214, 216,0], 
                    "Source Type/Orientation":  [216, 218,0],    
                    "Source Energy Direction":  [218, 224,0], 
                    "Source Measurement":  [224, 230,0],  
                    
                    "Source Measurement Unit":  [230, 232,0], 
                    "Unassigned":  [232, 240,0],                            
        
            }   #end of dictionary 

        return trace_head_dict