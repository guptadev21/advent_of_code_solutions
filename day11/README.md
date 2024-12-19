# [Day 11](https://adventofcode.com/2024/day/11)

 The problem revolves around an evolving set of stones, each engraved with a number. The stones change based on specific rules applied simultaneously at each step (or "blink"). The task is to determine the state and count of stones after a given number of blinks.

## Problem Description

You are observing a line of stones. Each stone is engraved with a number, and the stones evolve according to the following rules applied simultaneously:

1. **Rule 1**: If a stone is engraved with the number `0`, it is replaced by a stone engraved with the number `1`.
2. **Rule 2**: If a stone is engraved with a number that has an even number of digits, it splits into two stones:
   - The left half of the digits becomes the number engraved on the new left stone.
   - The right half of the digits becomes the number engraved on the new right stone.
   - Any leading zeroes are removed (e.g., `1000` splits into `10` and `0`).
3. **Rule 3**: If none of the above rules apply, the stone is replaced by a single stone with its number multiplied by `2024`.

### Additional Notes
- The stones maintain their order after transformation.
- The transformation process happens simultaneously for all stones.

## Example

### Initial Arrangement:
```
125 17
```

### After 1 Blink:
- `125` (odd digits) is multiplied by `2024` to become `253000`.
- `17` (odd digits) is multiplied by `2024` to become `1` and `7` (split).

```
253000 1 7
```

### After 2 Blinks:
- `253000` (even digits) splits into `253` and `000` (leading zeroes removed, `0`).
- `1` (odd digits) is multiplied by `2024` to become `2024`.
- `7` (odd digits) is multiplied by `2024` to become `14168`.

```
253 0 2024 14168
```

### Subsequent Blinks:
The process continues similarly, applying the rules to each stone.

## Objective

Given an initial arrangement of stones, determine:
1. How many stones will exist after 25 blinks?
2. How many stones will exist after 75 blinks?

## Example Calculation

### Input:
```
Initial stones: 125 17
```

### Output After 25 Blinks:
```
Number of stones: 55312
```

### Output After 75 Blinks:
```
Number of stones: TBD
```

## Results

### Test Cases
1. **Input**: `0 1 10 99 999`
   - **Output After 1 Blink**: `1 2024 1 0 9 9 2021976`

2. **Input**: `125 17`
   - **Output After 25 Blinks**: `55312`

3. **Input**: (Longer Simulation for 75 Blinks)
   - **Output**: TBD

### Approach Overview

This program simulates the transformation of stones through a series of rules over 75 iterations while keeping track of how many times each type of stone appears.

#### Steps:
1. **Initialize Stones:**
   - Start with a list of initial stones.
   - Convert it into a dictionary where each unique stone is a key, and its value represents the count (initially 1 for all stones).

2. **Apply Rules:**
   - For each iteration (up to 75 times):
     - Create a new dictionary to store updated stones.
     - For each stone and its count in the current dictionary:
       - Apply transformation rules (`rule_1`, `rule_2`, `rule_3`) in sequence:
         - `rule_1`: If the stone is `0`, transform it into `1`.
         - `rule_2`: If the stone length is even, split it into two new stones.
         - `rule_3`: Multiply the stone value by 2024.
       - Update the new dictionary with the transformed stones and their counts.
     - Replace the current dictionary with the new one.

3. **Count Results:**
   - After 75 iterations, sum up the counts of all stones in the final dictionary.


This approach efficiently tracks and updates the transformations while ensuring the program handles large numbers and multiple iterations effectively.

