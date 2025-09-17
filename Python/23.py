'''
Non-Abundant Sums

Problem 23
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''

def proper_numbers(n):
    pn = set([1])
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            pn.add(i)
            if i != n // i:
                pn.add(n // i)
    return sorted(pn)

def is_abundant(num, pn):
    return num < sum(pn)

def main():
    # Converted to set for efficiency 
    abundant_numbers = set([x for x in range(1, input + 1) if is_abundant(x, proper_numbers(x))])
    
    total = 0
    for i in range(1, input + 1):
        pn_i = proper_numbers(i)
        abundant_divisors = list(set(pn_i) & set(abundant_numbers))
        print(f'{i} : PN: {pn_i} : AD: {abundant_divisors}')
        
        if len(abundant_divisors) != 0:
            for j in abundant_divisors:
                if i - j not in abundant_numbers:
                    total += i
                    print(f'{i} has Abundent Divsor {j}, however, cannot sum two abundent numbers. Total: {total}')
                    break
                else:
                    print(f'Invalid : {i} - {j} = {i-j}, which is Abundant')
        else:
            total += i
            print(f'{i} Total: {total}')
    
    print(f'Final total: {total}')

# First 15 Adundant Numbers for reference
# 12, 18, 20, 24, 30, 36, 40, 42, 48, 54, 56, 60, 66, 70, 72
if __name__ == '__main__':
    test = 100
    input = 28123

    main()