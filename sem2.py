a = int(input("Input your number: "))
i = 1
res = 1

while a != 0:
    res = res * i
    i = i + 1
    a = a - 1

print(res)

