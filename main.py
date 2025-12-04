with open("example.txt","r") as file:
    example4 = file.read()

with open("input.txt","r") as file:
    input4 = file.read()

data = input4
grid = data.split("\n")
last_column = len(grid[0]) - 1
last_row = len(grid) - 1
answer_a = 0
answer_b = 0

def check_position(row, column):
    global last_column, last_row, grid
    if row < 0 or column < 0 or row > last_row or column > last_column:
        return False
    else:
        if grid[row][column] == "@":
            return True
        else:
            return False

def check_around(position):
    rolls_around = 0
    if check_position(position[0] - 1, position[1] - 1):
        rolls_around += 1
    if check_position(position[0] - 1, position[1]):
        rolls_around += 1
    if check_position(position[0] - 1, position[1] + 1):
        rolls_around += 1
    if check_position(position[0], position[1] - 1):
        rolls_around += 1
    if check_position(position[0], position[1] + 1):
        rolls_around += 1
    if check_position(position[0] + 1, position[1] - 1):
        rolls_around += 1
    if check_position(position[0] + 1, position[1]):
        rolls_around += 1
    if check_position(position[0] + 1, position[1] + 1):
        rolls_around += 1
    if rolls_around < 4:
        return True
    else:
        return False

def remove_roll(position, list_grid):
    if list_grid[position[0]][position[1]] == "@":
        list_grid[position[0]] = list_grid[position[0]][:position[1]] + "." + list_grid[position[0]][position[1] + 1:]
        return list_grid
    else:
        return list_grid


removed = 1
iteration = 0
while removed > 0:
    rolls = []
    for current_row in grid:
        for index in range(len(current_row)):
            if current_row[index] == "@":
                pos = [grid.index(current_row), index]
                if check_around(pos):
                    rolls.append(pos)
                    if iteration == 0:
                        answer_a += 1
                    answer_b += 1
    for roll in rolls:
        grid = remove_roll(roll, grid)
    removed = len(rolls)
    iteration += 1

print(f"Answer A is: {answer_a}")
print(f"Answer B is: {answer_b}")