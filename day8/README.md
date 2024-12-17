# [Day8](https://adventofcode.com/2024/day/8)

## Problem Statement

You are analyzing a grid containing multiple antennas. Each antenna is identified by a single **lowercase letter**, **uppercase letter**, or **digit**. The task is to identify unique locations where **antinodes** occur based on specific resonance conditions.

### Part One

For two antennas of the **same frequency**:
- An **antinodal point** occurs at a location that is perfectly **in line** with the antennas.
- The location must satisfy the condition where one antenna is **twice as far** as the other.

---

### Part Two

In addition to Part One rules:
- An **antinodal point** occurs at any position that lies **in line** with at least two antennas of the same frequency, regardless of distance.
- Antennas themselves are included as antinodes if they align with at least two others of the same frequency.

---

## Approach and Solution

### Overall Strategy

1. **Identify and Store Antenna Positions**:
   - Traverse the grid to identify the positions of all antennas.
   - Use a dictionary to group antennas by their **frequency** (character or digit).
     - Key: Antenna frequency
     - Value: List of positions (x, y) of antennas with that frequency.

2. **Calculate Antinode Points**:
   - For each frequency group, compute antinodal points based on the given conditions.

---

### Part One: Antinodal Points with "Twice the Distance" Condition

For each pair of antennas `(x, y)` and `(a, b)` of the same frequency:
- Use the following formulas to calculate the potential antinodal points:
  - **Point 1**: `(x + (x - a), y + (y - b))`
  - **Point 2**: `(a + (a - x), b + (b - y))`

These formulas determine positions that are collinear and satisfy the "twice the distance" condition.

- **Store the unique points** in a set to ensure no duplicates.

---

### Part Two: General Collinearity Using Slope and Intercept

For each pair of antennas `(x, y)` and `(a, b)` of the same frequency:
1. Compute the **slope** of the line connecting the antennas:
    ```math
        \text{slope} = \frac{\Delta y}{\Delta x} = \frac{b - y}{a - x}
    ```
2. Use the formula for the **y-intercept** (column position `j`) of the line at any row `i`:
   ```math
        j = \left( \frac{\Delta y}{\Delta x} \right) \times (i - x) + y
   ```
   - Iterate over rows and compute all collinear points.
   - Include antennas themselves if they satisfy the collinearity condition.

3. Store the **unique positions** in a set to ensure no duplicates.

---

### Steps in Code

1. **Grid Parsing**:
   - Read the grid and extract antenna positions.
   - Group antennas by frequency using a dictionary.

2. **Part One Calculations**:
   - For each pair of antennas in the same frequency group, apply the formulas to compute antinode points.

3. **Part Two Calculations**:
   - For each pair of antennas, compute collinear points using the slope-intercept formula.

4. **Result**:
   - Count the total number of **unique positions** containing antinodes.


---

## Summary

- **Part One**: Use the "twice the distance" formula to determine antinodes.
- **Part Two**: Use the slope-intercept formula to calculate general collinear points, including antenna positions.

By grouping antennas by frequency and systematically computing antinode positions, the solution efficiently calculates the total number of unique antinodal locations.
