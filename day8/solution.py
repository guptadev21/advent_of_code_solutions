# Store positions of the different antennas in a dictionary
def store_positions(input_str):
    positions = {}
    for i, row in enumerate(input_str.split("\n")):
        for j, column in enumerate(row):
            if column != ".":
                if column in positions:
                    positions[column] += [(i, j)]
                else:
                    positions[column] = [(i, j)]
    return positions


# size of map
def size_of_map(input_str):
    return len(input_str.split("\n")), len(input_str.split("\n")[0])


# count antinodes
def count_antinodes(input_str):
    positions = store_positions(input_str)
    n, m = size_of_map(input_str)
    antinodes = set()
    for i in positions:
        for j in range(len(positions[i])):
            for k in range(j + 1, len(positions[i])):
                antinode = antinodes_positions(positions[i][j], positions[i][k], n, m)
                if antinode:
                    if isinstance(antinode[0], tuple):
                        antinodes.add(antinode[0])
                        antinodes.add(antinode[1])
                    else:
                        antinodes.add(antinode)
    print(antinodes)
    return len(antinodes)


# count antinodes part 2
def count_antinodes_2(input_str):
    positions = store_positions(input_str)
    n, m = size_of_map(input_str)
    antinodes = set()
    for i in positions:
        for j in range(len(positions[i])):
            for k in range(j + 1, len(positions[i])):
                antinodes_temp = antinodes_position_2(
                    positions[i][j], positions[i][k], n, m
                )
                for antinode in antinodes_temp:
                    antinodes.add(tuple(antinode))

    print(antinodes)
    return len(antinodes)


# return antinodes positions
def antinodes_positions(pos1, pos2, n, m):
    x, y = pos1
    a, b = pos2
    antinode_pos1 = x + (x - a), y + (y - b)
    antinode_pos2 = a + (a - x), b + (b - y)

    if (
        antinode_pos1[0] < 0
        or antinode_pos1[0] >= n
        or antinode_pos1[1] < 0
        or antinode_pos1[1] >= m
    ) and (
        antinode_pos2[0] < 0
        or antinode_pos2[0] >= n
        or antinode_pos2[1] < 0
        or antinode_pos2[1] >= m
    ):
        print("0", antinode_pos1, antinode_pos2)
        return None

    elif (
        antinode_pos1[0] < 0
        or antinode_pos1[0] >= n
        or antinode_pos1[1] < 0
        or antinode_pos1[1] >= m
    ):
        return antinode_pos2

    elif (
        antinode_pos2[0] < 0
        or antinode_pos2[0] >= n
        or antinode_pos2[1] < 0
        or antinode_pos2[1] >= m
    ):
        return antinode_pos1

    return antinode_pos1, antinode_pos2


def antinodes_position_2(pos1, pos2, n, m):
    x, y = pos1
    a, b = pos2

    # slope
    dx = a - x
    dy = b - y

    antinodes = list()

    for i in range(n):
        # get the y-intercept for i
        j = (dy / dx) * (i - x) + y
        # check if the y-intercept is an integer
        if j.is_integer():
            if j >= 0 and j < m:
                antinodes.append([i, int(j)])

    return antinodes


example_input = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

actual_input = """Paste your input here"""


# n, m = size_of_map(actual_input)
# print(count_antinodes_2(actual_input))

n, m = size_of_map(example_input)
print(count_antinodes(example_input))
print(count_antinodes_2(example_input))
