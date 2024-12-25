# Open the input file
file = open("day14/input.txt", "r")

# Define the grid dimensions
n, m = 101, 103

# Read the input lines
lines = file.read().split("\n")

# Initialize position and velocity lists
p = []
v = []
for line in lines:
    # Split the line into position and velocity components
    line = line.strip().split(" ")
    line[0] = line[0].replace("p=", "").split(",")
    line[1] = line[1].replace("v=", "").split(",")
    # Append the position and velocity to their respective lists
    p.append([int(line[0][0]), int(line[0][1])])
    v.append([int(line[1][0]), int(line[1][1])])

# Initialize variables to track max and min product of quadrants
max_f = float("-inf")
min_f = float("inf")
max_s = None
min_s = None

# part 1
result = []
# Calculate the new positions of the robots at the current second
for i in range(len(p)):
    x, y = (p[i][0] + 100 * v[i][0]) % n, (p[i][1] + 100 * v[i][1]) % m
    result.append([x, y])

# Initialize quadrant counters
quad1 = 0
quad2 = 0
quad3 = 0
quad4 = 0
# Count the number of robots in each quadrant
for pos in result:
    if pos[0] < n // 2 and pos[1] < m // 2:
        quad1 += 1
    elif pos[0] < n // 2 and pos[1] > m // 2:
        quad2 += 1
    elif pos[0] > n // 2 and pos[1] < m // 2:
        quad3 += 1
    elif pos[0] > n // 2 and pos[1] > m // 2:
        quad4 += 1

print("Part 1")
print(quad1 * quad2 * quad3 * quad4)


# Iterate over each second up to n * m
for sec in range(n * m):
    result = []
    # Calculate the new positions of the robots at the current second
    for i in range(len(p)):
        x, y = (p[i][0] + sec * v[i][0]) % n, (p[i][1] + sec * v[i][1]) % m
        result.append([x, y])

    # Initialize quadrant counters
    quad1 = 0
    quad2 = 0
    quad3 = 0
    quad4 = 0
    # Count the number of robots in each quadrant
    for pos in result:
        if pos[0] < n // 2 and pos[1] < m // 2:
            quad1 += 1
        elif pos[0] < n // 2 and pos[1] > m // 2:
            quad2 += 1
        elif pos[0] > n // 2 and pos[1] < m // 2:
            quad3 += 1
        elif pos[0] > n // 2 and pos[1] > m // 2:
            quad4 += 1

    # Calculate the product of the number of robots in each quadrant
    temp_res = quad1 * quad2 * quad3 * quad4
    # Update max and min product and their corresponding seconds
    if temp_res > max_f:
        max_f = temp_res
        max_s = sec
    if temp_res < min_f:
        min_f = temp_res
        min_s = sec


print("Part 2: most probably second with minimum factor is answer.")
# Print the maximum and minimum product of quadrants and their corresponding seconds
print(max_f, max_s)
print(min_f, min_s)
