'''
Factorial Digit Sum

Problem 20
n! means n x (n - 1) x ... x 3 x 2 x 1.

For example, 10!, = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''
def factorial(n): # Recurive factorial
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def num_to_list(n):
    return list(map(int, str(n)))

def main():
    fact = factorial(input)
    print(sum(num_to_list(fact)))
    
if __name__ == "__main__":
    test = 10
    input = 100
    
    main()