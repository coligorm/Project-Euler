'''
Power Digit Sum

Problem 16

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2 ^ 1000?

Ans: 1366
'''
def pow_to_list(n):
    return list(map(int, str(pow(2, n))))

def main():
    print(sum(pow_to_list(input)))

if __name__ == "__main__":
    test = 15
    input = 1000
    main()