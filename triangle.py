def area(base,height):
    return base * height / 2

def perimeter(side1,side2,side3):
    return side1+side2+side3

def big(x):
    return (2*x)**x

import math

def area_hero(s1,s2,s3):
    '''
    (number,number,number) -> float
    
    Uses the heron's method to return the value of the area of the triangle
    
    >>> area_hero(3,4,5)
    6.0
    >>> area_hero(10.5,6,9.3)
    27.73168584850189
    '''
    semi = perimeter(s1,s2,s3)/2
    return math.sqrt(semi*(semi-s1)*(semi-s2)*(semi-s3))
