from formulas import *


while True:
    choice = input("Enter choice:")
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