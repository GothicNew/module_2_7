def print_params(a,b,c):
    print(a,b,c)


values_list = [14, "Строка", True]
values_dict = {'a': 1, 'b': 'Привет', 'c': True}
values_list_2 = [54.32, 'Hello']

print_params(*values_list_2, 42)

print_params(values_list[0], values_list_2[1], values_dict['b'])



