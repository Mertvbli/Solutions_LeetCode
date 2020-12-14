def reverse(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    if -2**31 <= x <= 2**31 - 1:
        x1 = int(str(x)[1:4])
        x2 = int(str(x1)[::-1])
        if x > 1:
            x3 = int(str(x)[::-1])
            if -2**31 <= x3 <= 2**31 - 1:
                return int(str(x)[::-1])
            else:
                return 0
        else:
            return '-' + str(x2)


print(reverse(-123))
print(reverse(123))
print(reverse(120))
print(reverse(0))
print(reverse(1534236469))
