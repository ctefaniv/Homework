def age_input():
    age = int(input("Enter your age:"))
    try:
        if age < 0:
            raise ValueError
        elif age % 2 == 0:
            print("Your age is even")
        else:
            print("Your age is odd")
    except ValueError:
        print("You not born yet")


age_input()
