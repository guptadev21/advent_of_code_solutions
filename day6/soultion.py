def parse_map(input_map):
    return [list(row) for row in input_map.splitlines()]

def print_map(map_grid):
    for row in map_grid:
        print("".join(row))

def find_person(map_grid):
    for r, row in enumerate(map_grid):
        for c, cell in enumerate(row):
            if cell in ['^', '>', '<', 'V']:
                return (r, c, cell)
    return None

def turn_right(direction):
    directions = ['^', '>', 'V', '<']
    return directions[(directions.index(direction) + 1) % 4]

def step_forward(row, col, direction):
    if direction == '^':
        return row - 1, col
    elif direction == '>':
        return row, col + 1
    elif direction == 'V':
        return row + 1, col
    elif direction == '<':
        return row, col - 1

def simulate_patrol(input_map):
    map_grid = parse_map(input_map)
    person_pos = find_person(map_grid)
    if not person_pos:
        raise ValueError("No person found on the map")

    row, col, direction = person_pos
    visited = set()
    state_history = set()  # Track (row, col, direction) to detect loops
    rows, cols = len(map_grid), len(map_grid[0])

    while 0 <= row < rows and 0 <= col < cols:
        if (row, col, direction) in state_history:
            return -1
        
        state_history.add((row, col, direction))
        visited.add((row, col))

        next_row, next_col = step_forward(row, col, direction)

        if (next_row >= rows or next_row < 0 or next_col >= cols or next_col < 0):
            break
        elif (0 <= next_row < rows and 0 <= next_col < cols and 
                map_grid[next_row][next_col] != '#'):
            row, col = next_row, next_col
        else:
            direction = turn_right(direction)


    return len(visited)

def find_loop_obstruction_positions(input_map):
    loop_sum = 0
    map_grid = parse_map(input_map)
    person_pos = find_person(map_grid)
    if not person_pos:
        raise ValueError("No person found on the map")

    rows, cols = len(map_grid), len(map_grid[0])
    # loop_positions = []

    for r in range(rows):
        for c in range(cols):
            if map_grid[r][c] == '.':
                # Temporarily place an obstruction
                map_grid[r][c] = '#'
                distinct_positions = simulate_patrol("\n".join("".join(row) for row in map_grid))

                if distinct_positions == -1:  # Check if loop forms
                    loop_sum += 1

                # Remove the obstruction
                map_grid[r][c] = '.'

    return loop_sum

# Example Input
example_input = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

input_map = """Put the input map here"""

# distinct_positions = simulate_patrol(input_map)
no_of_loops = find_loop_obstruction_positions(example_input)

# print(f"\nDistinct positions visited: {distinct_positions}")
print(f"Number of loops: {no_of_loops}")
