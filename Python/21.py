'''
Amicable Numbers

Problem 21
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''
import time

def proper_numbers(n):
    pn = set([1])
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            pn.add(i)
            if i != n // i:
                pn.add(n // i)
    return sorted(pn)

def amicable(x, y):
    return sum(proper_numbers(y)) == x and x != y

def main():
    # loop_counter = 0
    # avg_time = 0
    # while loop_counter < 10:
        start = time.time()
        # Use sets to avoid duplicates 
        amicable_pairs = set()
        for i in range(input):
            pn_sum = sum(proper_numbers(i))
            if amicable(i, pn_sum):
                amicable_pairs.add(i)
                amicable_pairs.add(pn_sum)
        print(f"Total: {sum(amicable_pairs)}")
    
        # end = time.time()
        # avg_time += end - start
        # loop_counter += 1
    
    # print(f"Average time = {avg_time / 10}")
    
    # Before optimisation: Avg 3.92 seconds
    # After optimisation: Avg 0.09 seconds
    
if __name__ == "__main__":
    test = 220
    input = 10000
    
    main()