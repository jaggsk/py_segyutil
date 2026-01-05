def segy_read_ebcdic_header(ebcdic_bin):   
        
    '''
    Method to convert ECDIC header from binary to ascii
    Input is the first 3200 byte package from the input file
    EBCDIC header is constructed from 40 lines, each containing a maximum of 80 chracters
    Conversion from binary to ascii using .decode('IBM500')
    Output is a 40 entry list, each entry  containing one 80 charater line
    KJAGGS Feb 2022
    '''
        
    #formats for line length
    #read 80 characters as 1 line and then shift 80 and read again
    line_length = 80
    first_character = 1
    last_character = 80
    #list to host ebcdic text lines
    ebcdic_list = []
    #ebcdic_list.append('01234567890123456789012345678901234567890123456789012345678901234567890123456789')
    #iterate through the 40 lines
    #capture next 80 byte binary package and decode
    #append new line to list
    for i in range(39):
        ebcdic_list.append(ebcdic_bin[first_character:last_character].decode('IBM500'))
        #print(self.ebcdic_bin[first_character:last_character].decode('IBM500'))
        first_character += line_length
        last_character += line_length

    return ebcdic_list