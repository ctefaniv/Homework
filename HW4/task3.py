n = int(input())
a = 0
b = 1
print(a, b, end=" ")
while a + b < n:
    a, b = b, a + b
    print(b, end=" ")
