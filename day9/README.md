# [Day 9](https://adventofcode.com/2024/day/9)

### Part 1 

The amphipod is trying to organize files on a hard drive, but their program isn't working. You step in to help!  

The **disk map** (your input) shows how files and free space are arranged. Here's how it works:  
- The numbers alternate between file size and free space size.  
  - For example, `12345` means:  
    - A 1-block file, 2 blocks of free space, a 3-block file, 4 blocks of free space, and a 5-block file.  
  - `90909` means three 9-block files with no free space between them.  

Each file gets an **ID** based on its order, starting with 0. So, for `12345`, the files are:  
- `0` → 1-block file  
- `1` → 3-block file  
- `2` → 5-block file  

If we represent this disk map visually (`.` = free space):  
- `12345` → `0..111....22222`  

The goal is to **compact the disk** by moving file blocks to the leftmost free space, one block at a time. For example:  
- Start: `0..111....22222`  
- After moving: `022111222......`  

Once all files are compacted, calculate the **filesystem checksum**. The checksum is the sum of multiplying each block’s **position** by its **file ID**. Ignore free spaces during the calculation.  

For example, after compacting:  
- Disk map: `0099811188827773336446555566`  
- Checksum: Sum of (position × file ID), like `0 * 0 + 2 * 9 + 4 * 8 + ...`  

Your task:  
1. Compact the disk.  
2. Calculate the resulting checksum.  
