# // Write a function to find the longest common prefix string amongst an array of strings.

# // If there is no common prefix, return an empty string "".

# // Example 1:

# // Input: ["flower","flow","flight"]
# // Output: "fl"
# // Example 2:

# // Input: ["dog","racecar","car"]
# // Output: ""
# // Explanation: There is no common prefix among the input strings.

class Solution:
    def longestCommonPrefix(strs):
        length = len(strs)
        if(length < 2):
            if(length == 1):
                return strs[0]
            else: return ""
        indices = 1
        check = strs[0][0:1]
        hold = ""
        end = False
        while(end == False):
            for i in range (1, length):
                slice = strs[i][0:indices]
                if(indices > len(strs[i])):
                    return hold
                elif(slice != check):
                    return hold
            hold = slice
            indices = indices + 1
            check = slice
            check = strs[0][0:indices]

s = Solution 
print(s.longestCommonPrefix(["flower", "flower", "flo"]))
print(s.longestCommonPrefix([]))
print(s.longestCommonPrefix(["flower", "flower"]))