
from math import sqrt
from nose.tools import assert_equal
class Solution(object):
    def pallette():
        print(sqrt(25))
        s = 'hello'
        print(s.upper())
    def sum(num1, num2):
        return num1+num2
    def testSum(sum):
        # Test whether sum is in fact 
        assert_equal(sum(2,2),4)
        assert_equal(sum(4,4),8)
        print("All Test Cases Passed")

s = Solution
# print(s.pallette())
print(s.testSum(s.sum))
