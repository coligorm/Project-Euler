'''
Smallest Multiple

Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Ans: 232792560

'''

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
            # print(pf)
            new_num /= i
        else:
            i += 1
            
    return pf

def prime_factors_list(nums):
    # Create a list of all prime factors for each given number
    pfs = []
    for i in nums:
        pfs.append(find_prime_factors(i))
        
    # print(f"Prime Factor list of {nums} = {pfs}")
    return pfs

def count_primes(l):
    occurrences = {}
    for x in l:
        if x not in occurrences.keys():
            occurrences[x] = 1
        else:
            occurrences[x] += 1
                
                
    # print(f"Occurrences of primes = {occurrences}")
    return occurrences

def main():
    prime_factors = prime_factors_list(input)
    
    # create a dictionary storing all the highest primes
    highest_primes =  {x:0 for x in range(20) if is_prime(x)}
    for primes in prime_factors:
        
        prime_dict = count_primes(primes)
        for key in prime_dict:
            
            if prime_dict[key] > highest_primes[key]:
                highest_primes[key] = prime_dict[key]      
    # print(f"Highest Prime Count \n{highest_primes}")
    
    # Using all prime numbers found as often as each occurs most often
    total = 1
    for key in highest_primes:
        if highest_primes[key] > 0:
            result = pow(key, highest_primes[key])
            # print(f"{total} x {result} = ")
            total *= result
        # print(total)
        
    print(f"LCM of {input} = {total}")

if __name__ == "__main__":
    test = [12,30] # LCM = 60
    input = range(1,21)
    
    main()