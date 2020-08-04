'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

'''

def reverse(self, x: int) -> int:
    negative = False
    if  x < 0:
        negative = True
        x = (-1)*x
    rev = 0 
    while x != 0:
        rev = (10*rev) + x%10
        x = x//10

    if rev >= (-1)*(2**31) and rev <= (2**31):
        if negative:
            return (-1)*rev
        else:
            return rev
    else:
        return 0
