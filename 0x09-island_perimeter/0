#!/usr/bin/python3
"""
0-island_perimeter
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.
    """
    perimeter = 0

    """ Define the height and width of the grid"""
    height = len(grid)
    width = len(grid[0])

    """ Define directions for adjacent cells: up, down, left, right"""
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    """ Iterate through each cell in the grid """
    for i in range(height):
        for j in range(width):
            """ Check only if the current cell is land """
            if grid[i][j] == 1:
                """ Initialize the count of contributing sides for this cell """
                sides = 0
                """ Check each direction """
                for dx, dy in directions:
                    """ Calculate the coordinates of the adjacent cell  """
                    x, y = i + dx, j + dy
                    """ Check if the adjacent cell is out of bounds or water """
                    if x < 0 or x >= height or y < 0 or y >= width or grid[x][y] == 0:
                        sides += 1
                """ Add the contributing sides to the perimeter """
                perimeter += sides

    return perimeter
