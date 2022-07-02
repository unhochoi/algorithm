input_list = [-8, -11, 5, -9, 4, 6]

input_list_sort = input_list.sort()

a = input_list[0] * input_list[1] * input_list[len(input_list)-1]
b = input_list[len(input_list)-3] * input_list[len(input_list)-2] * input_list[len(input_list)-1]

if (a>b):
    print(a)
else:
    print(b)

