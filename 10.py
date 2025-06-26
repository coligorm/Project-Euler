'''
Summation of Primes

Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

Ans: 142913828922
'''
import time

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

def main():
    start_time = time.time()

    # Starting at 2, the first prime, in other to increament for loop by 2
    sum = 2
    for i in range(3,input,2):
        if is_prime(i):
            sum += i
    
    end_time = time.time()
            
    print(f"The sum of prime numbers less than {input} = {sum}")
    print(f"Execution time: {end_time - start_time}")

if __name__ == "__main__":
    input = 2_000_000
    test = 10
    main()