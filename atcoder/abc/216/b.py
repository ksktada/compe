n = int(input())

name = []

for i in range(0, n):
    tmp = input()
    name.append(tmp)

for i in range(0, n):
    for j in range(0, n):
        if i != j and name[i] == name[j]:
            print("Yes")
            exit()
print("No")