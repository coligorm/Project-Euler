'''
Highly Divisible Triangular Number

Problem 12
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be
1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
1, 3, 6, 10, 15, 21, 28, 36., 45, 55, ... 

Let us list the factors of the first seven triangle numbers:
1 : 1
3 : 1, 3
6 : 1, 2, 3, 6
10: 1, 2, 5, 10
15: 1, 3, 5, 15
21: 1, 3, 7, 21
28: 1, 2, 4, 7, 14, 28
 
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?

Ans: 76576500

'''
import math

def find_triangle_number(n):
    triangle = 0
    for i in range(n + 1):
        triangle += i
    
    return triangle

def find_factor_pair(n, i):
    pair = []
    if n == i:
        pair.append(i)
    elif n % i == 0:
        pair.append(i)
        pair.append(n // i)

    return pair

def main():
    factors = []
    i = 1
    while len(factors) <= input:
        factors = []
        triangle = find_triangle_number(i)
        for j in range(1, int(math.floor(math.sqrt(triangle))) + 1):
            pair = find_factor_pair(triangle,j)
            if len(pair) > 0:
                factors.extend(pair)
        
        factors.sort()            
        # print(f"{triangle}: {factors}")
        i += 1
    
    print(f"\n{triangle} is the first triangle number to have over {input} divisors")

if __name__ == "__main__":
    test = 5
    input = 500
    main()