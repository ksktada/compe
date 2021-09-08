nm = input()
n, m = nm.split(" ")

n = int(n)
m = int(m)

a_array = [[]]

for i in range(0, m):
    k = int(input())
    for j in range(0, k):
        a = map(input())
        a_array[i].append(a)


