# Given a string, find the length of the longest substring without repeating characters.

# Example 1:

# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# Example 2:

# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # use sliding window technique
        # start left at 0 index
        # traverse through string
        # if character has been visited, move left to that character
        # increase len of longest substring
        # update current index of visited to right + 1
        
        visited = {}
        longestSubstring = 0
        left = 0
        
        for right, char in enumerate(s):
            if char in visited:
                left = max(visited[char], left)
                
            longestSubstring = max(longestSubstring, right - left + 1)
            visited[char] = right + 1
            
        return longestSubstring