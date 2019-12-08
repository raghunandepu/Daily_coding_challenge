"""Longest Palindromic Substring (Medium)
​
Write a function that, given a string, returns its longest palindromic substring. A palindrome is defined as a string that is written the same forward and backward. Assume that there will only be one longest palindromic substring.
​
Sample input: "abaxyzzyxf"
Sample output: "xyzzyx"
​
"""
# Time: O(n**2) | Space: O(n)

def longestPalindromicSubstring(string):
  currentLongest = [0, 1] #Let it be the first char for now
  for i in range(1, len(string)):
    odd = getLongestPalindromeFrom(string, i - 1, i + 1) # i-1 left index, i+1 right index
    even = getLongestPalindromeFrom(string, i-1, i)
    
    longest = max(odd, even, key = lambda x: x[1] - x[0])
    currentLongest = max(longest, currentLongest, key = lambda x: x[1] - x[0])
  return string[currentLongest[0]:currentLongest[1]]

def getLongestPalindromeFrom(string, leftIdx, rightIdx):
  while leftIdx >=0 and rightIdx < len(string):
    if string[leftIdx] != string[rightIdx]:
      break
    leftIdx -= 1
    rightIdx +=  1
  return [leftIdx + 1, rightIdx]
  
  
print (longestPalindromicSubstring("abaxyzzyxf"))