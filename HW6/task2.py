from math import pi


def rectangle_square():
    a = int(input("Enter width:"))
    b = int(input("Enter height"))
    return a * b


def triangle_square():
    a = int(input())
    h = int(input("Enter height:"))
    return (a * h) / 2


def circle_square():
    r = int(input("Enter radius:"))
    return round(pi * r ** 2)


while True:
    choice = input("Enter choice")
    if choice == 'square':
        print(rectangle_square())
        continue
    elif choice == 'triangle':
        print(triangle_square())
        continue
    elif choice == 'circle':
        print(circle_square())
        continue
    elif choice == 'exit':
        break
    else:
        print("Entered choice not found")
