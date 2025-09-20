'''
Lexicographic Permutations

Problem 24
A permutation is an ordered arrangement of objects.
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:
012   021   102   120   201   210
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

Ans: 2783915460
'''
from itertools import permutations  

def main():
    numbers = [int(x) for x in input]
    perm = sorted(list(permutations(numbers, len(numbers))))
    result = int(''.join(map(str, perm[((999_999))])))

    print(result)

if __name__ == '__main__':
    test = '012'
    input = '0123456789'

    main()