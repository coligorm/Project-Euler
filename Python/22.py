'''
Names Scores

Problem 22

Using names.txt, begin by sorting it into alphabetical order.
Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
For example, when the list is sorted into alphabetical order, COLIN,
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?

'''
def read_file(filename):
    data = []
    with open(filename, 'r') as file:
        return sorted(file.read().replace('"', '').split(','))

def alphabetical_value(word):
    val = [ord(char) - 96 for char in word.lower()]
    return sum(val)

def main():
    total = 0
    names = {}
    for i, name in enumerate(input, start=1):
        names[name] = i * alphabetical_value(name)
        total += names[name]

    print(total)

if __name__ == "__main__":
    test = read_file('input_files/22-test.txt')
    input = read_file('input_files/22-input.txt')

    main()