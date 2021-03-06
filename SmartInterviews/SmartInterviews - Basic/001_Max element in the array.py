# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-max-element
"""
Find maximum element from the given array of integers.

Input Format

First line of input contains N - the size of the array and second line contains the elements of the array.

Constraints

1 <= N <= 103 
-109 <= ar[i] <= 109

Output Format

Print the maximum element of array.

Sample Input 0

5
-2 -19 8 15 4
Sample Output 0

15
Explanation 0

Self Explanatory"""

def solution(arr, n):
    arr.sort()
    return arr[-1]

n = int(input())
arr = list(map(int, input().split()))
print (solution(arr, n))