with open("example.txt","r") as file:
    example5 = file.read()

with open("input.txt","r") as file:
    input5 = file.read()

data = input5
ranges = [r.split("-") for r in data.split("\n\n")[0].split("\n")]
ids = data.split("\n\n")[1].split("\n")
answer_a = 0
answer_b = 0
new_ranges = []

def is_fresh(item_id, item_range):
    if int(item_id) in range(int(item_range[0]), int(item_range[1]) + 1):
        return True
    else:
        return False

for id_range in ranges:
    lower = int(id_range[0])
    upper = int(id_range[1])

    if ranges.index(id_range) == 0:
        to_check = ranges[ranges.index(id_range) + 1:]
    else:
        to_check = new_ranges
        new_ranges = []

    for id_range2 in to_check:
        if is_fresh(lower,id_range2):
            lower = int(id_range2[0])
        if is_fresh(upper,id_range2):
            upper = int(id_range2[1])
        if not is_fresh(lower,id_range2) and not is_fresh(upper,id_range2):
            new_ranges.append(id_range2)
    new_ranges.append([lower,upper])

for ingredient_id in ids:
    for id_range in new_ranges:
        if is_fresh(ingredient_id, id_range):
            answer_a += 1
            break

for id_range in new_ranges:
    answer_b += int(id_range[1]) - int(id_range[0]) + 1

print(f"Answer A is: {answer_a}")
print(f"Answer B is: {answer_b}")

