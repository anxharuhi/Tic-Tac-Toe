user_input = input()

input_list = [int(n) for n in list(user_input)]
output_list = []

for i in range(len(input_list) - 1):
    output_list.append((input_list[i] + input_list[i + 1]) / 2)

print(output_list)
