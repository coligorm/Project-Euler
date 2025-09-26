'''
Reciprocal Cycles

Problem 26
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
1/2 = 0.5
1/3 = 0.(3)
1/4 = 0.25
1/5 = 0.2
1/6 = 0.1(6)
1/7 = 0.(142857)
1/8 = 0.125
1/9 = 0.(1)
1/10 = 0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

'''
from decimal import Decimal, getcontext

def guess_seq_len(seq):
    guess = 1
    max_len = len(seq) // 2
    for x in range(2, max_len):
        if seq[0:x] == seq[x:2*x]:
            return x
        elif seq[2:x] == seq[x:2*x]:
            return x

    return guess

def main():
    # Set Decimal to 1000 decimal places
    getcontext().prec = input
    
    d = 0
    
    # longest = 0
    # while longest < input:
    #     i = 2
    #     # Some code
    #     longest = len(recur)
    #     d = recur
        
    i = 2
    while i < test + 1:
        
        recur = []
        
        fraction = str(Decimal(1) / Decimal(i))
        # print(fraction)
        fractional = fraction[2:]
        # print("\nFRACTIONAL:")
        # print(fractional)
        digits = [int(x) for x in fractional]
        # print(digits)
        seq = guess_seq_len(digits)
        digits = ''.join(map(str, digits))
        # print(seq)
        if seq == 1:
            # digits = int(''.join(map(str, digits)))
            # print(digits)
            print(f'1/{i} = {fraction}')
        elif seq == 2:
            # print(digits[0:seq])
            print(f'1/{i} = 0.({digits[0]})')
        else:
            print(f'1/{i} = 0.({digits[0:seq]})')
        
        i += 1

if __name__ == '__main__':
    test = 10
    input = 1000

    main()