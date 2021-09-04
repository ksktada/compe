n = int(input())

a = ""

while(n != 0):
    if n % 2 == 0:
        n = n / 2
        a = "B" + a
    else:
        n = n - 1
        a = "A" + a
print(a)
