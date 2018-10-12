# 20.
# Valid Parentheses
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

# Example 1:

# Input: "()"
# Output: true
# Example 2:

# Input: "()[]{}"
# Output: true
# Example 3:

# Input: "(]"
# Output: false
# Example 4:

# Input: "([)]"
# Output: false
# Example 5:

# Input: "{[]}"
# Output: true

class Solution: 
    def isValid(s):
        # This solution creates a stack and a dictionary, and removes an element in the stack if it is found in 
        # a dictionary of acceptable answers
        dic={"(":")", "[":"]", "{":"}", ")":"(", "]":"[", "}":"{"}
        stack_str=[]
        if(len(s) != 0):
            stack_str.append(s[0])
        else: 
            return True
        for i in range(len(s)-1):
            # print('i is: ', i)
            # print('STACK_STR: ', stack_str)
            # print('S[i+1]: ', s[i+1])
            if stack_str!=[] and dic[stack_str[-1]]==s[i+1]:
                stack_str.pop()
            else:
                stack_str.append(s[i+1])
        if (len(stack_str) == 0):
            return True
        else: 
            return False

s = Solution
print(s.isValid("([)]"))

# After a bracket is opened: (
#     valid responses are: ), [, {