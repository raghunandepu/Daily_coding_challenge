# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-number-of-multiples/problem

"""
Given a positive integer - N. Print the number of multiples of 3, 5 between [1, N].

Input Format

Input contains positive integer - N.

Constraints

1 <= N <=1018

Output Format

Print the number of multiples of 3, 5 in range of 1 to N.

Sample Input 0

11
Sample Output 0

5
Explanation 0

Multiples of 3 and 5 in range of 1 to 11 are 3, 5, 6, 9, 10."""

import math
N = int(input())
def multiples(N):
    # No. of mutiple of 3 + Number of multiples of 5 - common multiples of 3 and 5
    return N//3 + N //5 - N // 15

print (multiples(N))