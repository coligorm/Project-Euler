'''
Largest Palindrome Product

Problem 4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.

Ans: 906609

'''

def is_palindrome(n):
    num = str(n)
    return num == num[::-1]

def palindrome_finder():
    a = 999
    b = 999
    while not is_palindrome(a*b):
        a -= 1
        # Check first two digits are not same. then resets and decrease b.
        # Ex: a = 989, b = 999. Then a = 999, b = 998 and continue the while loop
        if str(a)[0:1] != str(b)[0:1]:
            a = b
            b -= 1
        
    print(f"{a} x {b} = {a*b}")
    return a*b
  
def main():
    ans = palindrome_finder()
    print(f"{ans} is a palindrome? {is_palindrome(ans)}")

if __name__ == "__main__":
        
    main()