from math import sqrt, trunc
from nose.tools import assert_equal
import timeit
import functools


class Solution(object):

    def pallette():
        print(sqrt(25))
        s = 'hello'
        print(s.upper())

    ### BIG-O ###
    # 1 - Constant
            # log(n) - Logarithmic
            # n - linear
            # nlog(n) - log linear
            # n^2 - Quadratic
            # n^3 - Cubic
            # 2^n - Exponential

    def compare(func1, num1, func2, num2): 
            
        time1 = timeit.timeit(functools.partial(func1, num1))
        time2 = timeit.timeit(functools.partial(func2, num2))
        # print('function ', func1, ' runs with input of ', num1 ,' in ', time1)
        # print('function ', func2, ' runs with input of ', num2 ,' in ', time2)
        if (time1 > time2):
            speed = time1/time2
            return func2, ' is ', speed, 'X faster than ', func1
        if (time2 > time1): 
            speed = time2/time1
            return func1, ' is ', speed, 'X faster than ', func2
    
    def bigO_constant(values):
        # A function with a constant runtime
        print(values[0])

    def bigO_linear(values):
        for val in values:
            print(val)

    def bigO_quadratic(values):
        # O(n^2)
        for item_1 in values:
            for item_2 in values:
                print(item_1, item_2)
    
    def bigO_logN(values):
        x = values
        # while(x > 0):
            # y = 2 + 2
            # x = x # 2

    def print_once(values):
         # O(n)
        #linear runtime is n
        for val in values:
            print(val)

    def print_two(values):
        # O(n)
        # Runtime = 2n -> As runtime goes to infinity the constant will be dropped
        for val in values:
            print(val)
        for val in values:
            print(val)

    def comp(values):
        print(values[0]) #O(1)

        #### O(n/2) ... O(1/2 * n)
        midpoint = trunc(len(values)/2) 
        for val in values[:midpoint]:
            print(val)
        #### 
        for x in range(10): # O(10)
            print('hello world')
        # Big-0 -> O(1 + n/2 + 10) -> O(n)   

    def  matcher(values, match):
        # Big-O -> 
            # Best-Case -> O(1)
            # Worst-Case -> O(n)
        for item in values:
            if item == match:
                return True
        return False

    def create_list(n):
        # Size of the new_list object scales linearly
        new_list = []
        for num in range(n):
            new_list.append('num')
        return new_list

    def printer(n):
        # Time complexity = linear, 
        # space complexity = O(1)
        for x in range(10):
            print('Hello World')


    #### End BIG-O ####

    def sum(num1, num2):
        return num1+num2

    def sum1(n): 
        final_sum = 0
        for x in range(n+1):
            final_sum += x
        return final_sum
    
    def sum2(n):
        return (n*(n+1))/2

    def testSum(sum):
        # Test whether sum is in fact 
        assert_equal(sum(2,2),4)
        assert_equal(sum(4,4),8)
        print("All Test Cases Passed")


s = Solution
first = [1,2,3,4,5,6,7,8,9,10]
match = 1
# print(s.pallette())
# print(s.testSum(s.sum))
# print(s.sum1(10));
# print(s.sum2(10));
# print(s.compare(s.sum1, 10, s.sum2, 10))

#### BIG-O ####
# print(s.bigO_constant(first))
# print(s.bigO_linear(first))
# print(s.bigO_quadratic(first))
# print(s.print_once(first))
# print(s.print_two(first))
# print(s.comp(first))
# print(s.matcher(first, 1))
# print(s.create_list(5))
# print(s.printer(10))
print(s.bigO_logN(first))






