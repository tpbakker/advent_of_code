with open("example.txt","r") as file:
    example3 = file.read()

with open("input.txt","r") as file:
    input3 = file.read()

def get_largest_number(input_list, min_remaining):
    descending = sorted(input_list, reverse=True)
    remaining_nrs = []
    largest_nr = 0
    n = 0
    if min_remaining == 0:
        largest_nr = descending[n]
        remaining_nrs = input_list[input_list.index(largest_nr) + 1:]
    else:
        while len(remaining_nrs) < min_remaining:
            largest_nr = descending[n]
            remaining_nrs = input_list[input_list.index(largest_nr) + 1:]
            n += 1
    return {"largest_number": largest_nr, "remaining": remaining_nrs}

def get_joltage(bank, length):
    joltage = ""
    for n in reversed(range(length)):
        largest_nr = get_largest_number(bank, n)["largest_number"]
        bank = get_largest_number(bank, n)["remaining"]
        joltage += str(largest_nr)
    return joltage

data = input3
banks = data.split("\n")
banks_as_lists = [list(map(int, item)) for item in banks]
outputs_a = []
outputs_b = []

for bank in banks_as_lists:
    outputs_a.append(int(get_joltage(bank, 2)))

for bank in banks_as_lists:
    outputs_b.append(int(get_joltage(bank, 12)))

print(f"Answer A is: {sum(outputs_a)}")
print(f"Answer B is: {sum(outputs_b)}")
