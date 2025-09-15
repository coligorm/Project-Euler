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
    list_of_lists = []
    with open(filename, 'r') as file:
        for line in file:
            row = [int(num) for num in line.strip().split()]
            list_of_lists.append(row)
    return list_of_lists

def main():
    pass

if __name__ == "__main__":
    input = read_file('input_files/18-input.txt')
    
    main()