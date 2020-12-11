even_numbers = []
odd_numbers = []
prime_numbers = []
for i in range(1, 11):
    if i % 2 == 0:
        even_numbers.append(i)
    elif i % 3 == 0:
        odd_numbers.append(i)
    elif i % 2 != 0 and i % 3 != 0:
        prime_numbers.append(i)

print(even_numbers)
print(odd_numbers)
print(prime_numbers)
