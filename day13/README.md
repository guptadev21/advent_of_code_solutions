# [Day 13](https://adventofcode.com/2024/day/13)

Each claw machine contains a single prize. To win the prize, the claw must be positioned exactly above the prize on both the **X** and **Y** axes. Each machine has two buttons that move the claw in specific ways along the X and Y axes. The objective is to determine the smallest number of tokens required to win as many prizes as possible.

---

## Example
```
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
```

## Machine Configuration

For machine 1:
- **Button A** moves the claw by a specified number of units along the X and Y axes (e.g., `X+94, Y+34`).
- **Button B** moves the claw by a different specified number of units along the X and Y axes (e.g., `X+22, Y+67`).
- **Prize Location** is defined by its coordinates (`X`, `Y`), such as `X=8400, Y=5400`.

### Rules:
- To win a prize, the claw's position must match the prize's coordinates exactly.
- Each press of Button A or B costs a certain number of tokens:
  - Button A: 3 tokens per press.
  - Button B: 1 token per press.

---

## Objective

### Part One
1. Determine the maximum number of prizes that can be won across all machines.
2. Calculate the minimum number of tokens required to win all possible prizes.

### Part Two
1. Update the prize locations by adding `10,000,000,000,000` to both the X and Y coordinates of every prize.
2. Re-evaluate:
   - How many prizes can still be won.
   - The fewest tokens needed to win all possible prizes after the adjustment. 

---

This problem involves finding optimal button presses to align the claw with the prize, minimizing token usage while maximizing the number of prizes won.