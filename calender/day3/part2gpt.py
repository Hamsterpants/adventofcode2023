testinput = '/workspaces/adventofcode2023/calender/day3/testinput.txt'
input = '/workspaces/adventofcode2023/calender/day3/input.txt'

test = 0

file_path = testinput if test else input

with open(file_path, 'r') as file:
    lines = file.readlines()

grid = [list(line.strip()) for line in lines]

def sum_adjacent_numbers(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    # Directions for moving in the grid 
    directions = [
        (-1, -1),   (0, -1),    (1, -1),
        (-1, 0),                (1, 0),
        (-1, 1),    (0, 1),     (1, 1),
    ]
    visited = [[False] * cols for _ in range(rows)]

    # Helper function to perform DFS and find connected numbers
    def dfs(x, y):
        stack = [(x, y)]
        positions = []
        number = 0
        while stack:
            cx, cy = stack.pop()
            if visited[cx][cy]:
                continue
            visited[cx][cy] = True
            positions.append((cx, cy))
            number = number * 10 + int(grid[cx][cy])
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and grid[nx][ny].isdigit():
                    stack.append((nx, ny))
        return number, positions

    # Find all numbers and their positions
    numbers = []
    for i in range(rows):
        for j in range(cols):
            if grid[i][j].isdigit() and not visited[i][j]:
                number, positions = dfs(i, j)
                numbers.append((number, positions))

    # Find all symbols
    symbols = []
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '*':
                symbols.append((i, j))

    # Check each symbol for exactly 2 adjacent numbers and multiply them
    total_sum = 0
    for si, sj in symbols:
        adjacent_numbers = []
        for dx, dy in directions:
            ni, nj = si + dx, sj + dy
            if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj].isdigit():
                # Find which number is at (ni, nj)
                for num, pos in numbers:
                    if (ni, nj) in pos and num not in adjacent_numbers:
                        adjacent_numbers.append(num)
                        break
        if len(adjacent_numbers) == 2:
            product = adjacent_numbers[0] * adjacent_numbers[1]
            total_sum += product
            #print(f"Symbol at ({si}, {sj}) is next to numbers {adjacent_numbers[0]} and {adjacent_numbers[1]}, product: {product}")

    print(f"Total sum of products of numbers adjacent to '*': {total_sum}")

sum_adjacent_numbers(grid)
