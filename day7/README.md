# [Day 7](https://adventofcode.com/2024/day/7)

## Problem Statement

The engineers need to perform final calibrations, but some young elephants have stolen all the operators from their calibration equations! Your task is to determine which test values can be produced by placing any combination of operators into their calibration equations.

### Example

Given the following equations:

```
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
```

Each line represents a single equation. The test value appears before the colon, and the numbers after the colon need to be combined with operators to produce the test value.

### Operators

- Addition (+)
- Multiplication (*)

Operators are evaluated left-to-right, not according to precedence rules. Numbers cannot be rearranged.

### Example Solutions

Only three of the above equations can be made true by inserting operators:

1. `190: 10 19` can be solved by `10 * 19 = 190`.
2. `3267: 81 40 27` can be solved by `81 + 40 * 27` or `81 * 40 + 27`.
3. `292: 11 6 16 20` can be solved by `11 + 6 * 16 + 20`.

The total calibration result is the sum of the test values for the equations that can be true: `190 + 3267 + 292 = 3749`.

### Part Two

The engineers realized there is a third operator: concatenation (||), which combines digits into a single number. For example, `12 || 345` becomes `12345`.

Using this new operator, three more equations can be made true:

1. `156: 15 6` can be solved by `15 || 6 = 156`.
2. `7290: 6 8 6 15` can be solved by `6 * 8 || 6 * 15`.
3. `192: 17 8 14` can be solved by `17 || 8 + 14`.

Adding these to the previous results, the new total calibration result is `190 + 3267 + 292 + 156 + 7290 + 192 = 11387`.

Your task is to determine which equations can be true and calculate their total calibration result.