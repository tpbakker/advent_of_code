with open("example.txt","r") as file:
    example_day_2 = file.read()

with open("input.txt","r") as file:
    input_day_2 = file.read()

id_ranges = input_day_2.split(",")
invalid_ids_a = []
invalid_ids_b = []
max_length = 0

for id_range in id_ranges:
    id_range = id_range.split("-")
    lower_bound = int(id_range[0])
    upper_bound = int(id_range[1]) + 1
    for id_number in range(lower_bound, upper_bound):
        id_number = str(id_number)
        id_length = len(id_number)
        if len(id_number) > max_length:
            max_length = len(id_number)
        for n in range(2, max_length + 1):
            if id_length % n == 0:
                slice_length = int(id_length / n)
                slices = [id_number[i:i + slice_length] for i in range(0, id_length, slice_length)]
                if len(set(slices)) <= 1:
                    if n == 2:
                        invalid_ids_a.append(int(id_number))
                    if int(id_number) not in invalid_ids_b:
                        invalid_ids_b.append(int(id_number))

answer_a = sum(invalid_ids_a)
answer_b = sum(invalid_ids_b)

print(f"Answer A is: {answer_a}")
print(f"Answer B is: {answer_b}")