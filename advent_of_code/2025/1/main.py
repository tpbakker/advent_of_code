with open("example.txt","r") as file:
    example_day_1 = file.read()

with open("input.txt","r") as file:
    input_day_1 = file.read()

print(moves)
dial = 50
answer_a = 0
answer_b = 0

for rotation in moves:
    direction = rotation[0]
    amount = int(rotation[1:])
    if direction == 'R':
        for _ in range(amount):
            dial = (dial + 1) % 100
            if dial == 0:
                answer_b += 1
    else:
        for _ in range(amount):
            dial = (dial - 1) % 100
            if dial == 0:
                answer_b += 1
    if dial == 0:
        answer_a += 1

print(f"Answer A is: {answer_a}")
print(f"Answer B is: {answer_b}")
