# Advent of Code - Day 2 - Part One

cubes_in_bag = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

def result(input):
    games_passed = 0
    for game in input:
        is_possible = True
        n_game, sets = game.split(':')
        sets = sets.strip().split(';')
        for set in sets:
            cubes_color = set.split(',')
            for cubes in cubes_color:
                amount, color = cubes.strip().split(' ')
                if cubes_in_bag[color] < int(amount):
                    is_possible = False
                    break
        if is_possible:
            games_passed += int(n_game.split(' ')[1])
    return games_passed
