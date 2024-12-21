# [Day 12](https://adventofcode.com/2024/day/12)

This program calculates the cost of fencing garden regions based on two different pricing models.

### Problem Overview

Each garden plot is represented by a single letter on a map, indicating the type of plant. Adjacent plots (horizontally or vertically) with the same type of plant form a **region**. The program computes the total cost of fencing these regions using two different methods.

### Key Concepts

1. **Area**: The number of plots in a region.
2. **Perimeter**: The number of sides of plots in a region that do not touch other plots of the same type.
3. **Number of Sides**: The total number of straight fence sections enclosing a region.

---

### Part 1: Cost Using Perimeter

- **Price Formula**: `Price = Area × Perimeter`
- **Example**:

   **Map**:
   ```
   AAAA
   BBCD
   BBCC
   EEEC
   ```

   **Calculation**:
   - Region A: Area = 4, Perimeter = 10, Price = `4 × 10 = 40`
   - Region B: Area = 4, Perimeter = 8, Price = `4 × 8 = 32`
   - Region C: Area = 4, Perimeter = 10, Price = `4 × 10 = 40`
   - Region D: Area = 1, Perimeter = 4, Price = `1 × 4 = 4`
   - Region E: Area = 3, Perimeter = 8, Price = `3 × 8 = 24`

   **Total Price**: `40 + 32 + 40 + 4 + 24 = 140`

---

### Part 2: Cost Using Number of Sides

- **Price Formula**: `Price = Area × Number of Sides`
- **Example**:

   **Same Map**:
   ```
   AAAA
   BBCD
   BBCC
   EEEC
   ```

   **Calculation**:
   - Region A: Area = 4, Sides = 4, Price = `4 × 4 = 16`
   - Region B: Area = 4, Sides = 4, Price = `4 × 4 = 16`
   - Region C: Area = 4, Sides = 8, Price = `4 × 8 = 32`
   - Region D: Area = 1, Sides = 4, Price = `1 × 4 = 4`
   - Region E: Area = 3, Sides = 4, Price = `3 × 4 = 12`

   **Total Price**: `16 + 16 + 32 + 4 + 12 = 80`

---

### Usage

1. Input the garden map as a grid of letters.
2. The program will calculate:
   - Total price using **perimeter** (Part 1).
   - Total price using **number of sides** (Part 2).
3. Output both results for comparison. 

This allows you to evaluate fencing costs under different pricing models effectively!