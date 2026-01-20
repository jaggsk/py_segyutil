def byte_adjustment(first_byte=None,last_byte=None):

    '''
    convert byte positiions from true to python position syntax
    Read Bytes 1-4 returns 0 and 4
    start read at byte zero, include 4 bytes
    '''

    return first_byte - 1, (last_byte - first_byte) + 1