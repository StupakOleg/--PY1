list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение
number_of_first_max_value = 0
first_max_value = list_numbers[number_of_first_max_value]
length = len(list_numbers)
for index, value in enumerate(list_numbers):
    if value > first_max_value:
        number_of_first_max_value = index
        first_max_value = list_numbers[number_of_first_max_value]
_replace_tuple = first_max_value, list_numbers[length - 1]
list_numbers[number_of_first_max_value], list_numbers[length - 1] = _replace_tuple[1], _replace_tuple[0]
print(list_numbers)
