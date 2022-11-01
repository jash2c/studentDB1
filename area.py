def area(base,height):
    '''(number, number) -> number
    return the area of a triangle with dimensions base and height.

    >>> area(1,2)
    1.0

    '''
    return base*height/2

def perimeter(s1,s2,s3):
    '''
    (number,number,number) -> number

    Returns the total length of all sides of the triangle.

    >>> perimeter(1,2,3)
    6
    >>> perimeter(1,1,1)
    3
    '''
    return s1+s2+s3


def semiperimeter(s1,s2,s3):
    '''
    (number,number,number) -> float

    Returns half of the perimeter of a triangle.
    
    >>> semiperimeter(1,2,3)
    3
    >>> semiperimeter(1.2,2,3)
    3.1 '''
    return perimeter(s1,s2,s3)/2

def convert_to_minutes(hours):
    '''(int) -> int
    Returns converted number of minutes from a number of hours.

    >>> convert_to_minutes(1)
    60
    >>> convert_to_minute(2.5)
    150
    '''
    result = hours*60
    return result
