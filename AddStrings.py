'''
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

'''

    def addStrings(self, num1: str, num2: str) -> str:
        #123
        # 98
        #221 
        res = ""
        carry = 0
        i = len(num1) - 1
        j = len(num2) - 1
        while i >=0 or j >=0 or carry >0:
            if i>=0:
                carry += int(num1[i])
                i -= 1
            if j>=0:
                carry += int(num2[j])
                j -= 1
            res += str(carry%10)
            carry = carry//10
        return res[::-1]
