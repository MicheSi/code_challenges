# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: "cbbd"
# Output: "bb"

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # if string is empty, return the empty string
        # loop through letters in string
        # check through each substring to see if it's a palindrome
        # return longest palindrome length
        if s == '':
            return s
        for i in range(len(s)):
            length = len(s) - i
            
            left = 0
            right = len(s) - length + 1
            
            currStr = ''
            
            for char in range(left, right):
                if char == 0:
                    currStr = s[char:char + length]
                else:
                    currStr = currStr[1:] + s[char + length - 1]
                    
                if currStr == currStr[::-1]:
                    return currStr