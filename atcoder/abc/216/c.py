n = int(input())

a = "A"
b = 1

if n == 1:
    print("A")
    exit()

if n == 2:
    print("AB")
    exit()

if n == 3:
    print("AAA")
    exit()

if n == 4:
    print("AAB")
    exit()

if n == 5:
    print("AABA")
    exit()

is_even = True

if n % 2 == 0:
    n = int(n / 2)
else:
    n = int((n - 1) / 2)
    is_even = False

while(b != n):
    b = b * 2

    if b < n:
        a = a + "B"
    else:
        b = int(b / 2)
        c = n - b

        for i in range(0, c):
            a = a + "A"
        break

a = a + "B"
print(a)