with open("example.txt","r") as file:
    example6 = file.read()

with open("input.txt","r") as file:
    input6 = file.read()

data = input6
rows = data.split("\n")
numbers = []
numbers_a = [[int(string) for string in x.split()] for x in data.split("\n")[:-1]]
numbers_b = []
modifiers_a = rows[-1].split()
modifiers_b = []
width = 0
answer_a = 0
answer_b = 0

def calculate_problem(index, a_or_b):
    global modifiers_a, modifiers_b, numbers_a, numbers_b
    if a_or_b == "a":
        calculation = f"{numbers_a[0][index]}"
        for x in range(1, len(numbers_a)):
            calculation += f"{modifiers_a[index]} {numbers_a[x][index]}"
        return eval(calculation)
    elif a_or_b == "b":
        calculation = f"{numbers_b[index][0]}"
        for x in range(1, len(numbers_b[index])):
            if numbers_b[index][x] != "":
                calculation += f"{modifiers_b[index]} {numbers_b[index][x]}"
        print(f"{calculation} = {eval(calculation)}")
        return eval(calculation)

    else:
        return None

for row in rows:
    if len(row) > width:
        width = len(row)

for n in reversed(range(width)):
    number = ""
    for m in range(len(rows)):
        try:
            if m == len(rows) - 1:
                if rows[m][n] != " ":
                    modifiers_b.append(rows[m][n])
            else:
                number += f"{rows[m][n]}"
        except IndexError:
            number += ""

    if number.isspace():
        numbers_b.append(numbers)
        numbers = []
    elif number:
        numbers.append(number.strip())
numbers_b.append(numbers)

for n in range(len(numbers_a)):
    answer_a += calculate_problem(n, "a")

for n in range(len(numbers_b)):
    answer_b += calculate_problem(n, "b")

print(f"Answer A is: {answer_a}")
print(f"Answer B is: {answer_b}")
