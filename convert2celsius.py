def convert_to_celsius(fdeg):
    '''
(number) - > number

Converts farentheight to celsius

>>> convert_to_celsius(32)
0
>>> convert_to_celsius(212)
100
    '''
    cdeg=(int(fdeg)-32)*(5/9)
    return int(cdeg)

