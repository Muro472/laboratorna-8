def recursion(n):
    if n == 0:
        return 0
    elif n == 1:
        return 9
    else:
        return (2 * recursion(n - 1) + 3 * recursion(n - 2))

num = int(input("значення n"))
print(recursion(num))