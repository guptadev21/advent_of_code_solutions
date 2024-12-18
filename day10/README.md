# [Day 10](https://adventofcode.com/2024/day/10)

This project focuses on analyzing topographic maps to identify hiking trails and calculate scores and ratings for trailheads. A trailhead is a starting position for one or more hiking trails. The program processes topographic maps and computes specific metrics based on the characteristics of the trails.

---

## Problem Description

### Topographic Map
- The map represents heights using a scale from `0` (lowest) to `9` (highest).
- Each position can be traversed up, down, left, or right, but diagonal movement is not allowed.
- Impassable tiles may exist but do not appear on actual maps.

### Hiking Trail
- A hiking trail starts at a height of `0` and ends at a height of `9`.
- The trail's height increases exactly by `1` at each step.
- A trailhead is any position of height `0` that starts one or more hiking trails.

---

## Metrics

### Trailhead Score
- **Definition**: The number of height-`9` positions reachable from a trailhead via hiking trails.
- Example:
  ```
  ...0...
  ...1...
  ...2...
  6543456
  7.....7
  8.....8
  9.....9
  ```
  The trailhead at height `0` has a score of `2` because two height-`9` positions are reachable.

### Trailhead Rating
- **Definition**: The number of distinct hiking trails that begin at a trailhead.
- Example:
  ```
  .....0.
  ..4321.
  ..5..2.
  ..6543.
  ..7..4.
  ..8765.
  ..9....
  ```
  The trailhead at height `0` has a rating of `3` because there are three distinct hiking trails leading to height-`9` positions.

---

## Goals

1. **Calculate the sum of all trailhead scores**: Identify all trailheads and compute the total number of reachable height-`9` positions.
2. **Calculate the sum of all trailhead ratings**: Determine the total number of distinct hiking trails starting from all trailheads.

---

### Example
For the larger example:
```
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
```
- **Part 1 Output**: 36 (sum of scores).
- **Part 2 Output**: 81 (sum of ratings).

