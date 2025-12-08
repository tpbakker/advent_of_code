with open("example.txt","r") as file:
    example6 = file.read()

with open("input.txt","r") as file:
    input6 = file.read()

data = input6
rows = data.split("\n")
ints = [[int(string) for string in x.split()] for x in rows[:-1]]
length = len(ints[0])
modifiers = rows[-1].split()
results_a = []
answer_a = 0
answer_b = 0

def calculate_problem(n):
    global ints, modifiers
    calculation = f"{ints[0][n]} {modifiers[n]} {ints[1][n]} {modifiers[n]} {ints[2][n]} {modifiers[n]} {ints[3][n]}"
    return eval(calculation)

for n in range(length):
    results_a.append(calculate_problem(n))

print(f"Answer A is: {sum(results_a)}")
print(f"Answer B is: {answer_b}")
