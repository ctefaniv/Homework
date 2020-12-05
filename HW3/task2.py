number = 6753
number = list(map(int, str(number)))
total = 1
for i in number:
    total *= i
print("Добуток цифр:", total)


def convert_list(number):
    num = int(''.join(map(str, number)))
    return num


number.reverse()
print(convert_list(number))
number.sort()
print(convert_list(number))







