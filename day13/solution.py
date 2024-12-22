from sympy import symbols, solve

x, y = symbols("x y")


def part_1(machine):
    # Initialize token spend counter
    token_spend = 0

    # Split the machine input into lines
    lines = machine.split("\n")
    eqs = []

    # Parse Button A coordinates
    A = lines[0].split(": ")[1].split(", ")
    A[0] = A[0].split("X+")[1] + "*x"
    A[1] = A[1].split("Y+")[1] + "*x"
    print(A)

    # Parse Button B coordinates
    B = lines[1].split(": ")[1].split(", ")
    B[0] = B[0].split("X+")[1] + "*y"
    B[1] = B[1].split("Y+")[1] + "*y"
    print(B)

    # Parse Prize coordinates
    reward = lines[2].split(": ")[1].split(", ")
    reward[0] = reward[0].split("X=")[1]
    reward[1] = reward[1].split("Y=")[1]

    # Create equations based on parsed coordinates
    eq1 = A[0] + "+" + B[0] + "-" + reward[0]
    eq2 = A[1] + "+" + B[1] + "-" + reward[1]
    eqs.append(eq1)
    eqs.append(eq2)
    print(eqs)

    # Solve the equations
    res = solve(eqs)

    # Check if the solutions are integers and calculate token spend
    if res[x] % 1 == 0 and res[y] % 1 == 0:
        token_spend += (3 * res[x]) + res[y]

    return token_spend


def part_2(machine):
    # Initialize token spend counter
    token_spend = 0

    # Split the machine input into lines
    lines = machine.split("\n")
    eqs = []

    # Parse Button A coordinates
    A = lines[0].split(": ")[1].split(", ")
    A[0] = A[0].split("X+")[1] + "*x"
    A[1] = A[1].split("Y+")[1] + "*x"
    print(A)

    # Parse Button B coordinates
    B = lines[1].split(": ")[1].split(", ")
    B[0] = B[0].split("X+")[1] + "*y"
    B[1] = B[1].split("Y+")[1] + "*y"
    print(B)

    # Parse Prize coordinates and add a large number to them
    reward = lines[2].split(": ")[1].split(", ")
    reward[0] = reward[0].split("X=")[1]
    reward[0] = str(int(reward[0]) + 10000000000000)
    reward[1] = reward[1].split("Y=")[1]
    reward[1] = str(int(reward[1]) + 10000000000000)

    # Create equations based on parsed coordinates
    eq1 = A[0] + "+" + B[0] + "-" + reward[0]
    eq2 = A[1] + "+" + B[1] + "-" + reward[1]
    eqs.append(eq1)
    eqs.append(eq2)
    print(eqs)

    # Solve the equations
    res = solve(eqs)

    # Check if the solutions are integers and calculate token spend
    if res[x] % 1 == 0 and res[y] % 1 == 0:
        token_spend += (3 * res[x]) + res[y]

    return token_spend


example_input = """
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""

total_token_1 = 0
total_token_2 = 0

actual_input = open("day13/input.txt").read()

# machines = actual_input.strip().split('\n\n')

machines = example_input.strip().split("\n\n")


for machine in machines:
    total_token_1 += part_1(machine)
    total_token_2 += part_2(machine)

print(total_token_1)
print(total_token_2)
