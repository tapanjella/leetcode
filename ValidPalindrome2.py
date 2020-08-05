'''
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:

Input: "aba"
Output: True
Example 2:

Input: "abca"
Output: True
Explanation: You could delete the character 'c'.

'''
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l<r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return s[l:r] == s[l:r][::-1] or s[l+1:r+1] == s[l+1:r+1][::-1]
        return True
