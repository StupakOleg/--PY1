from random import shuffle, sample


def get_unique_list_numbers() -> list[int]:
    list_ = [number for number in sample(range(-10, 11), 15)]
    shuffle(list_)
    return list_


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
