# http://www.spoj.com/problems/PRIME1/
"""
Peter wants to generate some prime numbers for his cryptosystem. Help him! Your task is to generate all prime numbers between two given numbers!

Input

The input begins with the number t of test cases in a single line (t<=10). In each of the next t lines there are two numbers m and n (1 <= m <= n <= 1000000000, n-m<=100000) separated by a space.

Output

For every test case print all prime numbers p such that m <= p <= n, one number per line, test cases separated by an empty line.

Example

Input:
2
1 10
3 5

Output:
2
3
5
7

3
5
Warning: large Input/Output data, be careful with certain languages (though most should be OK if the algorithm is well designed)"""
import math

def primes(start, end):
  result = []
  for ele in range(start, end + 1):
    if ele > 1:
      for n in range(2, int(math.sqrt(ele))+1):
        if (ele % n)  == 0:
          break
      else:
        result.append(ele)
  return result

t = int(input())
for tc in range(t):
  start, end = map(int, input().split())
  result = primes(start, end)
  for e in result:
    print (e)
  