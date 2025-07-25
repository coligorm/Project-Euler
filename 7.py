'''
10 001st Prime

Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10,001st prime number?

Ans: 104743
'''

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
    count = 0
    prime = 0
    num = 1
    while count != input:
        if is_prime(num):
            count += 1
            prime = num
        if count < 3:
            num += 1
        else:
            num += 2
                
    print(f"The prime number at position {input} = {prime}")

if __name__ == "__main__":
    test = 6
    input = 10001
    
    main()