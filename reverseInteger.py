
# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:

# Input: 123
# Output: 321
# Example 2:

# Input: -123
# Output: -321
# Example 3:

# Input: 120
# Output: 21
class Algos():
    def reverse(self, x):
        s = str(x)
        if x>=0: 
            res = int(s[::-1])
            return res
        else: 
            res = int(s[::-1][0:len(s) - 1]) * (-1)
        if res in range(-2**31,2**31):
            return res
        else: 
            return 0

a = Algos()
print(a.reverse(-123))