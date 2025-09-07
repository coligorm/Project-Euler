'''
Largest Prime Factor

Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?

Ans: 6857

'''

def is_prime(n) : 
  
    # Corner cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True

    # This is checked so that we can skip  
    # middle five numbers in below loop 
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

def main():
    primefactors = find_prime_factors(input)
    print(primefactors)
    
    print(f"Largest prime factor of the number {input} = {max(primefactors)}")
    
    
if __name__ == "__main__":
    
    input = 600851475143
    
    main()