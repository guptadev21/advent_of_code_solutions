from progressbar import ProgressBar
from collections import defaultdict

def rule_1(stone):
    if stone == '0':
        return ['1']
    return [stone]

# Split the number in two numbers in the current position
def rule_2(stone):
    if len(stone) % 2 == 0:
        half = len(stone) // 2
        return [str(int(stone[:half])), str(int(stone[half:]))]
    return [stone]

# Number multiplied by 2024
def rule_3(stone):
    return [str(int(stone) * 2024)]

def step_stone(stone):
    results = rule_1(stone)
    if results == [stone]:
        results = rule_2(stone)
        if results == [stone]:
            results = rule_3(stone)
    return results

def apply_rules(input_stones, max_iterations):
    stones = {stone: 1 for stone in input_stones}

    progress = ProgressBar(maxval=max_iterations).start()
    for iteration in range(max_iterations):
        new_stones = defaultdict(int)
        for stone, count in stones.items():
            for new_stone in step_stone(stone):
                new_stones[new_stone] += count
        stones = new_stones
        progress.update(iteration + 1)

    return sum(stones.values())

example_input = '125 17'
actual_input = 'Paste your input here'

initial_stones = example_input.split(' ')
# initial_stones = actual_input.split(' ')

result = apply_rules(initial_stones, 'No. of iterations')
print("\nResult:", result)
