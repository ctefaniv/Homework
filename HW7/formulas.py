from math import pi
from math import pow


def rectangle_square():
    a = int(input("Enter width:"))
    b = int(input("Enter height:"))
    return a * b


def triangle_square():
    a = int(input())
    h = int(input("Enter height:"))
    return (a * h) / 2


def circle_square():
    r = int(input("Enter radius:"))
    return round(pi * pow(r, 2))
