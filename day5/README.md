# [Day 5](https://adventofcode.com/2024/day/5)

#### Part 1
The North Pole printing department is in full swing, preparing safety manuals for the upcoming sleigh launch. However, the Elf operating the printer is having trouble ensuring the pages print in the right order. Since the safety manual is critical for a smooth sleigh launch, you step in to help.

The rules are simple but strict: for certain pairs of page numbers, if both pages are part of the update, one must always come before the other. For example, the rule `X|Y` means page `X` must be printed **before** page `Y` if both appear in the update.

Your task is to check whether the updates provided are already in the correct order based on these rules. If they are, you also need to find the **middle page number** for each correctly-ordered update (the middle page is the one at the center of the update list when ordered). Finally, calculate the total of all the middle page numbers from the correctly-ordered updates.

#### Part 2
Once you've identified the correctly-ordered updates, it's time to fix the rest. For each **incorrectly-ordered update**, reorder the pages according to the rules to make them valid.

After reordering these updates, find the middle page numbers for each corrected update and calculate the total of these middle page numbers.

In short:
- **Part 1**: Find and validate the correctly-ordered updates and sum their middle page numbers.
- **Part 2**: Fix the incorrectly-ordered updates, find their middle page numbers, and sum them.