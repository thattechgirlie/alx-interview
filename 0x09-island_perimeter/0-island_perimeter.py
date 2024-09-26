#!/usr/bin/python3
""" 0-island_perimeter.py"""
 
def island_perimeter(grid):
    """
    returns the perimeter of the island
    described in grid
    """
    area = 0
    for row in grid + list(map(list, zip(*grid))):
        for i1, i2 in zip([0] + row, row + [0]):
            area += int(i1 != i2)
    return area