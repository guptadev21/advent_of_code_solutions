def convert_data(input_data):
    data = []
    for i in range(len(input_data)):
        if i % 2 == 0:
            id = str(i // 2)
            data.extend([id] * int(input_data[i]))
        elif i % 2 == 1:
            data.extend(["."] * int(input_data[i]))

    return data


# Part One function
def compact_disc(data):
    copy_data = data.copy()

    i = 0
    j = len(copy_data) - 1

    while i < j:
        if copy_data[i] == "." and copy_data[j] != ".":
            # Swap file data from `j` to `i`
            copy_data[i], copy_data[j] = copy_data[j], copy_data[i]
            i += 1
            j -= 1
        elif copy_data[i] != ".":
            # Move `i` forward if it's already a file
            i += 1
        elif copy_data[j] == ".":
            # Move `j` backward if it's a free space
            j -= 1

    # Convert digits to integers after compacting
    for k in range(len(copy_data)):
        if copy_data[k].isdigit():
            copy_data[k] = int(copy_data[k])

    return copy_data


# Part Two function
def compact_disc_by_file(data):
    copy_data = data.copy()
    n = len(copy_data)

    # Step 1: Identify file blocks and their sizes
    file_positions = []  # [(start_index, file_id, size), ...]
    free_blocks = []  # [(start_index, size), ...]

    i = 0
    while i < n:
        if copy_data[i].isdigit():
            start = i
            file_id = int(copy_data[i])
            while i < n and copy_data[i] == str(file_id):
                i += 1
            file_positions.append((start, file_id, i - start))
        else:
            start = i
            while i < n and copy_data[i] == ".":
                i += 1
            free_blocks.append((start, i - start))

    # Step 2: Process files in reverse order of file ID
    file_positions.sort(key=lambda x: x[1], reverse=True)  # Highest file ID first

    for start, file_id, size in file_positions:
        # Try to find the leftmost free span large enough for this file
        for j, (free_start, free_size) in enumerate(free_blocks):
            if (
                free_size >= size and free_start < start
            ):  # Free span must be left of the file
                # Move the file
                for k in range(size):
                    copy_data[free_start + k] = str(file_id)
                # Clear the old file location
                for k in range(start, start + size):
                    copy_data[k] = "."
                # Update free_blocks to reflect the new free span sizes
                free_blocks[j] = (free_start + size, free_size - size)
                free_blocks.append((start, size))  # Add the freed space back
                free_blocks.sort()  # Keep free blocks sorted by position
                break  # File has been moved, move to the next file

    # Convert digits to integers after compacting
    for k in range(len(copy_data)):
        if copy_data[k].isdigit():
            copy_data[k] = int(copy_data[k])

    return copy_data


def sum_data(data):
    sum = 0
    for i in range(len(data)):
        if data[i] == ".":
            continue
        if isinstance(data[i], int):
            sum += data[i] * i
    return sum


# example_input = """2333133121414131402"""

# data = list(example_input)

file = open("./day9/input.txt", "r")

data = file.read()

converted_list_data = convert_data(data)

# Part 1
print(compact_disc(converted_list_data))
print(sum_data(compact_disc(converted_list_data)))


# Part 2
print(compact_disc_by_file(converted_list_data))
print(sum_data(compact_disc_by_file(converted_list_data)))
