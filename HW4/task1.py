number = int(input())
fact = 1
if number < 0:
    print("Factorial for negative number don't exist")
else:
    for i in range(1, number + 1):
        fact *= i
    print(fact)
