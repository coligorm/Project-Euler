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

def find_seq_len(seq):
    seq_len = 0
    max_len = len(seq) // 2
    
    if len(seq) > 1:
        for x in range(2, input):
            if seq[0:x] == seq[x:2*x]:
                seq_len = x
            elif seq[2:x] == seq[x:2*x]:
                seq_len = x

            # Remove first digit from list and see if any repeats
            if x == max_len:
                seq = seq[1:]
                max_len - 1
                
                for y in range(2, max_len + 1):
                    if seq[0:y] == seq[y:2*y]:
                        seq_len = y
                    elif seq[2:y] == seq[y:2*y]:
                        seq_len = y
                    
                    # If the repeat happens after the first digit, flag with -1
                    if y > max_len // 2:
                        if seq[1:y+1] == seq[y:2*y]:
                            return -1
            
    return seq_len

def find_recur(l):
    recur = []
    seq_len = find_seq_len(l)
    max_len = seq_len // 2
    
    if not seq_len:
        print("No repeats")
    elif seq_len == -1:
        if len(set(l[1:max_len])) == 1: # All elements are the same
            print('same')
            recur.append(l[2])
        else:
            recur.append(list(set(l)))
            print('not same')
    else:
        recur.append(l[0:seq_len])
    
    return recur
    
    # # print(seq)
    # if not seq:
    #     # digits = int(''.join(map(str, digits)))
    #     # print(digits)
    #     print(f'1/{i} = {fraction}')
    # elif seq == 2:
    #     # print(digits[0:seq])
    #     print(f'1/{i} = 0.({digits[0]})')
    # elif seq == -1:
    #     print(f'1/{i} = 0.{digits[0]}({digits[2]})')
    # else:
    #     print(f'1/{i} = 0.({digits[0:seq]})')

def main():
    # Set Decimal to 1000 decimal places
    getcontext().prec = input
    
    for i in range(2, test + 1):
        fraction = str(Decimal(1) / Decimal(i))
        # print(fraction)
        fractional = fraction[2:]
        # print("\nFRACTIONAL:")
        # print(fractional)
        digits = [x for x in fractional]
        print(digits)
        print(find_recur(digits))
    d = 0
    
    # longest = 0
    # while longest < input:
    #     i = 2
    #     # Some code
    #     longest = len(recur)
    #     d = recur

if __name__ == '__main__':
    test = 10
    input = 1000

    main()