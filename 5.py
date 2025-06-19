'''
Smallest Multiple

Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Ans:

'''
from collections import Counter

# Finding the LCM of 1-20
# List all prime factors of 1-20
# Multiply the most occurances of each prime factor

def is_prime(n) : 
    # Corner cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True

    # This is checked so that we can skip  
    # 1 - 4 in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False

    i = 5
    while (i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i += 6

    return True

def find_prime_factors(num):
    # Check base case: if n itself is prime
    if (is_prime(num)) :
        return [num]
    
    pf = []
    i = 2
    new_num = num
    
    while i**2 <= num:
        if (new_num % i == 0) and (is_prime(i)):
            pf.append(i)
            print(pf)
            new_num /= i
        else:
            i += 1
            
    return pf

def prime_factors_dict(keys):
    # Create a dictionary of all prime factors for each given number
    d = dict.fromkeys(keys,0)
    for k in d:
        d[k] = find_prime_factors(k)
        
    print(d)

def count_primes(d):
    occurrences = {}
    for v in d.values():
        for i in v:
            v.count(i)


def main():
    pfd = prime_factors_dict(input)
    count_primes(pfd)


if __name__ == "__main__":
    input = [12,30]
    
    main()