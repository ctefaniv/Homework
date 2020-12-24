def day():
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    try:
        num = int(input("Enter number:"))
        if num > 7 or num < 1:
            raise ValueError
        else:
            print(f"It's {weekdays[num - 1]}")
    except ValueError:
        print("Enter correct number")


day()

