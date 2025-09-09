'''
Number Letter Counts

Problem 17
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 
3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 
115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.

Ans: 21124
'''

from num2words import num2words

def gather_numbers(n):
    words = []
    for i in range(1,n+1):
        words.append(num2words(i))
    return words

def main():
    words = gather_numbers(input)
    count = 0
    for word in words:
        if ' ' in word or '-' in word:
            word = word.replace(' ', '').replace('-', '')
        count += len(word)
    print(f'There are {count} letters used from the numbers 1 to {input}')

if __name__ == "__main__":
    test = 5
    input = 1000
    main()