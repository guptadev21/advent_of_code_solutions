def operator_or(a, b):
    return int(f"{a}{b}")


def add_mul_concat(test_case, nums, res, position):
    # Base case: if the current position is equal to the length of nums,
    # check if the current result (res) is equal to the test_case.
    if position == len(nums):
        return res == test_case

    # Recursive case: try three different operations (multiplication, addition, and operator_or)
    # on the current result (res) with the current element in nums.
    # If any of these operations lead to a solution, return True.
    return (
        add_mul_concat(test_case, nums, res * nums[position], position + 1)
        or add_mul_concat(test_case, nums, res + nums[position], position + 1)
        or add_mul_concat(
            test_case, nums, operator_or(res, nums[position]), position + 1
        )
    )


example_input = """7290: 6 8 6 15
156: 15 6
292: 11 6 16 20
190: 10 19
3267: 81 40 27
83: 17 5
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13"""

file = open("./day7/input.txt", "r")
actual_input = file.readlines()

total_sum = 0

# for row in example_input.split("\n"):
for row in actual_input:
    test_case, nums = row.split(":")
    test_case = int(test_case)
    nums = list(map(int, nums.split()))
    if add_mul_concat(test_case, nums, nums[0], 1):
        total_sum += test_case
    else:
        if len(nums) == 2 and test_case == operator_or(nums[0], nums[1]):
            total_sum += test_case
        for i in range(len(nums) - 2):
            copy_nums = nums[:i] + [operator_or(nums[i], nums[i + 1])] + nums[i + 2 :]
            if add_mul_concat(test_case, copy_nums, copy_nums[0], 1):
                total_sum += test_case

print(total_sum)
