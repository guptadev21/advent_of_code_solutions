def get_path_1(map, position, path_count, visited):
    flag = False
    n, m = len(map), len(map[0])
    x, y = position
    if map[x][y] == "9" and (x, y) not in visited:
        visited.append((x, y))
        return path_count + 1

    if (y < m - 1) and (int(map[x][y + 1]) == int(map[x][y]) + 1):
        path_count += get_path_1(map, (x, y + 1), 0, visited)
        flag = True
    if (y > 0) and (int(map[x][y - 1]) == int(map[x][y]) + 1):
        path_count += get_path_1(map, (x, y - 1), 0, visited)
        flag = True
    if (x < n - 1) and (int(map[x + 1][y]) == int(map[x][y]) + 1):
        path_count += get_path_1(map, (x + 1, y), 0, visited)
        flag = True
    if (x > 0) and (int(map[x - 1][y]) == int(map[x][y]) + 1):
        path_count += get_path_1(map, (x - 1, y), 0, visited)
        flag = True
    if not flag:
        return 0

    return path_count


def get_path_2(map, position, path_count):
    flag = False
    n, m = len(map), len(map[0])
    x, y = position
    if map[x][y] == "9":
        return path_count + 1

    if (y < m - 1) and (int(map[x][y + 1]) == int(map[x][y]) + 1):
        path_count += get_path_2(map, (x, y + 1), 0)
        flag = True
    if (y > 0) and (int(map[x][y - 1]) == int(map[x][y]) + 1):
        path_count += get_path_2(map, (x, y - 1), 0)
        flag = True
    if (x < n - 1) and (int(map[x + 1][y]) == int(map[x][y]) + 1):
        path_count += get_path_2(map, (x + 1, y), 0)
        flag = True
    if (x > 0) and (int(map[x - 1][y]) == int(map[x][y]) + 1):
        path_count += get_path_2(map, (x - 1, y), 0)
        flag = True
    if not flag:
        return 0

    return path_count


example_input = """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""

actual_input = open("./day10/input.txt").read()

# map = example_input.strip().split('\n')
map = actual_input.strip().split("\n")

trailhead_count = 0
path_count = 0
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == "0":
            # print(i, j)
            trailhead_count += get_path_1(map, (i, j), 0, [])
            path_count += get_path_2(map, (i, j), 0)

print(trailhead_count)
print(path_count)
