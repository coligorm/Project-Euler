'''
Special Pythagorean Triplet

Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2.

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

Ans: 31875000
'''
# Pythagorean triplet can be written as:
# a = 2mn
# b = m^2 - n^2
# c = m^2 + n^2
# Therefore, 2mn + m^2 - n^2 + m^2 + n^2= 1000
# Thus, 2mn + 2m^2 = 1000

# I want m = 20 and n =5

def calc_a(m,n):
    return 2 * m * n

def calc_b(m,n):
    return pow(m,2) - pow(n,2)

def calc_c(m,n):
    return pow(m,2) + pow(n,2)

def create_triplet(a,b,c):
    return list((a,b,c))

def is_Pythagorean_triplet(l):
    if l == sorted(l) and (pow(l[0],2) + pow(l[1],2) == pow(l[2],2)):
        return True
    else:
        return False  

def product(l):
    total = 1
    for digit in l:
        total = total * digit
    return total
 
def main():
    m = 2
    n = 1
    while True:
        a = calc_a(m,n)
        b = calc_b(m,n)
        c = calc_c(m,n)
        if is_Pythagorean_triplet(create_triplet(a, b, c)) and a + b + c == 1000:
            break
        else:

            if m - n < 15:
                m += 1
            else:
                n += 1
    
    print(a,b,c)
    print(product(create_triplet(a,b,c)))

if __name__ == "__main__":
    input = 1000
    # test = [3,4,5]
    test = [200,375,425] # 40,000, 140,625, 180,625
    main()