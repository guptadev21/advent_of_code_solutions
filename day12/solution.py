from collections import deque

#  This functions groups the same type of plants in a dict with the key being the plant type and the value being a list of tuples with the coordinates of the plant in the bed.
def regions_dict(bed):
    regions = []
    
    seen_or_visited = set()
    for r in range (len(bed)):
        for c in range(len(bed[0])):
            region = set()
            region.add((r, c))
            if (r, c) in seen_or_visited: continue
            seen_or_visited.add((r, c))
            q = deque([(r, c)])
            while q:
                cr, cc = q.popleft()
                for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nr, nc = cr + dr, cc + dc
                    if nr < 0 or nc < 0 or nr >= len(bed) or nc >= len(bed[0]): continue
                    if bed[nr][nc] == bed[r][c] and (nr, nc) not in seen_or_visited:
                        region.add((nr, nc))
                        seen_or_visited.add((nr, nc))
                        q.append((nr, nc))
            regions.append(region)
    return regions

def perimeter(region):
    perimeter = 0
    for r, c in region:
        sides = 4
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if (nr, nc) in region:
                sides -= 1
        perimeter += sides
    return perimeter

# This functions will get corners for each region in bed
def corners_dict(region):
    corners = set()
    
    for r, c in region:
        # here cr, cc are coordinates of corners of a cell
        for cr, cc in [(r-0.5, c-0.5), (r+0.5, c-0.5), (r+0.5, c+0.5), (r-0.5, c+0.5)]:
            corners.add((cr, cc))
            
    # lets iterate over the corners and see if cells are avialable in which direction
    corners_count = 0
    for cr, cc in corners:
        config_for_cells = []
        for sr, sc in [(cr-0.5, cc-0.5), (cr+0.5, cc-0.5), (cr+0.5, cc+0.5), (cr-0.5, cc+0.5)]:
            config_for_cells.append((sr, sc) in region)
            
        if sum(config_for_cells) == 1 or sum(config_for_cells) == 3:
            corners_count += 1
        elif sum(config_for_cells) == 2:
            if config_for_cells[0] == config_for_cells[2] and config_for_cells[1] == config_for_cells[3]:
                corners_count += 2
                
    return corners_count
    
    

example_input = """
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""

actual_input = open('day12/input.txt').read()

bed = example_input.strip().split('\n')
# bed = actual_input.strip().split('\n')

regions = regions_dict(bed)

total_cost_part1 = 0
total_cost_part2 = 0

for region in regions:
    print('-'*10)
    for x, y in region:
        print(bed[x][y])
        break
    print(region)
    perimeter_cost = perimeter(region)
    total_cost_part1 += len(region)*perimeter_cost
    corners = corners_dict(region)
    total_cost_part2 += len(region)*corners

print("Part 1:", total_cost_part1)
print("Part 2:", total_cost_part2)