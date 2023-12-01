# Advent of Code - Day 1 - Part One

def result(input):
    '''
    Return the result of the puzzle for the given input.
    The input is a list of strings
    '''
    values = []
    for value in input:
        numbers = [x for x in value if x.isdigit()]
        values.append(int(numbers[0] + numbers[-1]))

    return sum(values)

if __name__ == '__main__':
    with open('./resources/input.txt', 'r') as f:
        input = f.read()
    print(result(input))
