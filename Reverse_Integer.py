#  Given a 32-bit signed integer, reverse digits of an integer.

# Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1].
# For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


class Solution:
    def reverse(self, x: int) -> int:
        x1 = int(str(abs(x))[::-1])
        if x1 >= 2**31 - 1 or x1 <= -2**31:
            return 0
        if x > 0:
            return x1
        else:
            return -x1

# Examples
print(reverse(-123))
print(reverse(123))
print(reverse(120))
print(reverse(0))
print(reverse(1534236469))
