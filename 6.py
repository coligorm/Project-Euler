'''
Sum Square Difference

Problem 6
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385.

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025.

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

Ans: 25164150

'''
def sum_of_squares(num):
    total = 0
    for i in range(num):
        total += pow(i, 2)

    return total

def square_of_sums(num):
    total = 0
    for i in range(num):
        total += i
    
    return pow(total, 2)

def main():
    
    # print(f"The sum of the squares of the first {input-1} numbers is = {sum_of_squares(input)}")
    # print(f"The square of the sum of the first {input-1} numbers is = {square_of_sums(input)}")
    print(f"The difference between the sum of the squares of the first {input-1} natural numbers and the square of the sum is\n{square_of_sums(input)} - {sum_of_squares(input)} = {square_of_sums(input)-sum_of_squares(input)}.")

if __name__ == "__main__":
    input = 101
    
    main()