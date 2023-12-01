# Advent of Code - Day 1 - Part Two

str2num_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0'
}

def result(input):
    '''
    Return the result of the puzzle for the given input.
    The input is a list of strings
    '''
    values = []
    for value in input:
        numbers = []
        for idx in range(len(value)):
            if value[idx].isdigit():
                numbers.append(value[idx])
            for num_str in str2num_dict:
                try:
                    if value[idx:idx+len(num_str)] == num_str:
                        numbers.append(str2num_dict[num_str])
                except IndexError:
                    pass
        values.append(int(numbers[0] + numbers[-1]))
    return sum(values)

if __name__ == '__main__':
    with open('./resources/input.txt', 'r') as f:
        input = f.read()
    print(result(input))
