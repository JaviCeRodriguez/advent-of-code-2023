# Advent of Code - Day 2 - Part Two
from functools import reduce

def result(input):
    power_sum = 0
    for game in input:
        set_cubes = {}
        _, sets = game.split(':')
        sets = sets.strip().split(';')
        for set in sets:
            cubes_color = set.split(',')
            for cubes in cubes_color:
                amount, color = cubes.strip().split(' ')
                color_in_game = color in set_cubes
                if (color_in_game and set_cubes[color] < int(amount)) \
                    or (not color_in_game):
                    set_cubes[color] = int(amount)
        power_sum += reduce(lambda x, y: x*y, set_cubes.values())
    return power_sum