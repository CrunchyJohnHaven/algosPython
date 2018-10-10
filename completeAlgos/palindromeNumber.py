# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

# Example 1:

# Input: 121
# Output: true
# Example 2:

# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# Follow up:

# Coud you solve it without converting the integer to a string?

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_str = str(x)
        print('STR(X): ', str(x))
        total_len = len(x_str)
        print('TOTAL_LEN: ', total_len)
        if total_len == 1:
            print()
            return True
        # If odd, theres a halfpoint, this index isn't included
        # If even, theres just two halfed strings
        x_str_1 = x_str[0:total_len//2]
        print('x_str_1: ', x_str_1)
        x_str_2 = x_str[-(total_len//2):] # Tail of string to halfpoint/halfed
        print('x_str_2: ', x_str_2)
        if x_str_1 == x_str_2[::-1]: # x_str_2[::-1] reverses string
            print(x_str_2[::-1])
            return True
        return False

s = Solution()
print(s.isPalindrome("racecar"))

