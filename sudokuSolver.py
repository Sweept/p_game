import numpy

grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]

numpy_grid = numpy.matrix(grid)
print(numpy_grid)

# y & x are the positions, n is the number at that position
# First checks the row
# Second checks the column
# Third checks the 3x3 square


def possible(y, x, n):
    global grid
    # First
    for i in range(0, 9):
        if grid[y][i] == n:
            return False
    # Second
    for i in range(0, 9):
        if grid[i][x] == n:
            return False
    # Third
    x0 = (x//3) * 3
    y0 = (y//3) * 3

    for i in range(0, 3):
        for j in range(0, 3):
            if grid[y0+i][x0+j] == n:
                return False

    return True


print(possible(4, 4, 3))
print(possible(4, 4, 5))
