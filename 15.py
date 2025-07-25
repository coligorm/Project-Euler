'''
Lattice Paths

Problem 15

Starting in the top left corner of a 2 x 2 grid,
and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

_ _  _    _
   |  |_   |
   |    |  |_  etc.


How many such routes are there through a 20 x 20 grid?
'''

# The odd numbered rows of pascals triangle gives the answers
# to the number of moves for the corresponding grid.
# i.e. 
# 1 x 1 grid = 3rd row of pascal's triangle
# 2 x 2 grid = 5th row of pascal's triangle
# 3 x 3 grid = 7th row etc.

from math import factorial

def pascal(n):
    triangle = {}
    for i in range(n):
        row = []
        for j in range(i+1):
            

            # nCr = n!/((n-r)!*r!)
            row.append((factorial(i) // (factorial(j) * factorial(i-j))))
            
        print(row)

def main():
    pascal(5)

if __name__ == "__main__":
    test = 2
    input = 20  
    main()