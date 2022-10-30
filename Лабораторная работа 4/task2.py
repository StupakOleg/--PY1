QUANTITY = 0


def get_count_char(str_):
    quantity_dict = {}
    ready_string = (str_.replace(' ', '')).lower()
    for char in ready_string:
        if char.isalpha():
            quantity_dict[char] = quantity_dict.get(char, QUANTITY) + 1
    return quantity_dict


def get_frequency_char(str_):
    frequency_dict = get_count_char(str_)
    summary_quantity_chars = sum(frequency_dict.values())
    for char in frequency_dict:
        frequency_dict[char] /= summary_quantity_chars
    return frequency_dict


def get_percentage_char(dict_):   # Аргумент - словарь частот get_frequency_char(main_str)
    for char in dict_:
        dict_[char] *= 100
    return dict_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
