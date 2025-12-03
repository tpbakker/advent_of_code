with open("example.txt","r") as file:
    example3 = file.read()

with open("input.txt","r") as file:
    input3 = file.read()

def get_largest_number(input_bank: list, min_remaining: int):
    descending_bank = sorted(input_bank, reverse=True)
    remaining = []
    largest_number = 0
    index = 0
    if min_remaining == 0:
        largest_number = descending_bank[index]
        remaining = input_bank[input_bank.index(largest_number) + 1:]
    else:
        while len(remaining) < min_remaining:
            largest_number = descending_bank[index]
            remaining = input_bank[input_bank.index(largest_number) + 1:]
            index += 1
    return {"largest_number": largest_number, "remaining": remaining}

def get_joltage(input_bank: list, length: int):
    joltage = ""
    for n in reversed(range(length)):
        largest_nr = get_largest_number(input_bank, n)["largest_number"]
        input_bank = get_largest_number(input_bank, n)["remaining"]
        joltage += str(largest_nr)
    return joltage

data = input3
banks = data.split("\n")
banks_as_lists = [list(map(int, item)) for item in banks]
outputs_a = []
outputs_b = []

for bank in banks_as_lists:
    outputs_a.append(int(get_joltage(bank, 2)))
    outputs_b.append(int(get_joltage(bank, 12)))

print(f"Answer A is: {sum(outputs_a)}")
print(f"Answer B is: {sum(outputs_b)}")
