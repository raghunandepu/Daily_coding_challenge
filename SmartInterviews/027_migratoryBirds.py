# https://www.hackerrank.com/challenges/migratory-birds/problem
"""You have been asked to help study the population of birds migrating across the continent. Each type of bird you are interested in will be identified by an integer value. Each time a particular kind of bird is spotted, its id number will be added to your array of sightings. You would like to be able to find out which type of bird is most common given a list of sightings. Your task is to print the type number of that bird and if two or more types of birds are equally common, choose the type with the smallest ID number.
For example, assume your bird sightings are of types . There are two each of types  and , and one sighting of type . Pick the lower of the two types seen twice: type .
Function Description
Complete the migratoryBirds function in the editor below. It should return the lowest type number of the most frequently sighted bird.
migratoryBirds has the following parameter(s):
arr: an array of integers representing types of birds sighted
Input Format
The first line contains an integer denoting , the number of birds sighted and reported in the array . 
The second line describes  as  space-separated integers representing the type numbers of each bird sighted.
Constraints

It is guaranteed that each type is , , , , or .
Output Format
Print the type number of the most common bird; if two or more types of birds are equally common, choose the type with the smallest ID number.
Sample Input 0
6
1 4 4 4 5 3
Sample Output 0
4"""

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    bird_freq = [0, 0, 0, 0, 0, 0]
    for i in range(len(arr)):
        bird_freq[arr[i]] += 1
    return bird_freq.index(max(bird_freq))

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    #fptr.write(str(result) + '\n')
    print(str(result) + '\n')

    #fptr.close()