### [Day6](https://adventofcode.com/2024/day/6)

#### **Part 1: Counting Distinct Positions Visited**
The first task is to determine how many unique positions the person visits while patrolling the map. The movement rules are:
1. If there’s an obstacle (`#`) directly in front of the person, they turn right 90 degrees.
2. Otherwise, they move one step forward in the direction they are facing (`^`, `>`, `<`, or `V`).

The simulation tracks all positions visited by the person, stopping when they leave the map or get stuck in a loop. The goal is to output the count of distinct positions visited.

---

#### **Part 2: Finding Positions to Cause a Loop**
The second task is to find all positions on the map where placing a new obstruction (`#`) would cause the person to get stuck in an infinite loop. 

Steps to solve this:
1. Temporarily place an obstruction (`O`) at an empty spot (`.`).
2. Simulate the patrol. If the person ends up revisiting the same position and direction repeatedly (a loop), mark the spot as a potential obstruction.
3. Repeat this for every possible empty spot and record all such positions.

The output highlights these positions (`O`) on the map, and the program lists how many such obstructions are possible.