'''
Amicable Numbers

Problem 21
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''
def proper_numbers(n):
    pn = set([1])
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            pn.add(i)
            if i != n // i:
                pn.add(n // i)
    return sorted(pn)

def amicable(x, y):
    return sum(proper_numbers(x)) == y and sum(proper_numbers(y)) == x and x != y

def main():
    # Use sets to avoid duplicates 
    amicable_pairs = set()
    for i in range(input):
        pn_sum = sum(proper_numbers(i))
        if amicable(i, pn_sum):
            amicable_pairs.add(i)
            amicable_pairs.add(pn_sum)
    print(f"Total: {sum(amicable_pairs)}")
    
if __name__ == "__main__":
    test = 220
    input = 10000
    
    main()