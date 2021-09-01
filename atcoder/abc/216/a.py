a = str(input())
a1, a2 = a.split(".")
x = int(a1)
y = int(a2)

if 0 <= y and y <= 2:
    print(f'{x}-')
elif 3 <= y and y <=6:
    print(f'{x}')
else:
    print(f'{x}+')
