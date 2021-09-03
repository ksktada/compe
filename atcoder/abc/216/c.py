n = int(input())

a = "A"

if n == 1:
    print("A")
    exit()

if n%2 != 0:
    n = n - 1

while(n != 1):
    a = a + "B"
    n = n / 2
print(a)