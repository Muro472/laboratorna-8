def isperpendicular (a,b):
    return a[0] * b[0] + a[1] * b[1] == 0

n = int(input('Enter n = '))
a = [[float(input("a[{0}][{1}]=".format(i, j))) for j in range(3)] for i in range(n)]
b = 0
for el in a:
    print(el)

for i in range(n - 1):
    for j in range(i + 1,n):
        if (isperpendicular(a[i],a[j])):
            b += 1
print(b)