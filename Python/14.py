'''
Longest Collatz Sequence

Problem 14
The following iterative sequence is defined for the set of positive integers:
    n -> n/2 (n is even)
    n -> 3n + 1(n is odd)
Using the rule above and starting with 13, we generate the following sequence:
    13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

Ans: 837799

'''
def if_even(n):
    return n // 2

def if_odd(n):
    return (3 * n) + 1

def next_sequence(n):
    if n % 2 == 0:
        n = if_even(n)
    else:
        n = if_odd(n)
    return n

def main():
    longest = 0
    chain = []
    ans = 0
    
    i = test
    for n in range(test, goal):
        while n > 1:
            chain.append(n)
            n = next_sequence(n)

        curr = len(chain) + 1
        if curr > longest:
            longest = curr
            print(f"Found longer sequence: {i} with length {curr}")
            ans = i

        chain = []
        i += 1

    print(f"/nThe starting number {ans} produces the longest chain, under one million")

if __name__ == "__main__":
    test = 13
    goal = 1_000_000
    
    main()