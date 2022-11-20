import json


INPUT_FILE = "input.csv"


def csv_to_list_dict(filename: str, delimiter=",") -> list[dict]:
    with open(filename) as f:
        string_quantity = sum(1 for _ in f)
    with open(filename) as f:
        main_list = [(iteration.rstrip()).split(delimiter) for iteration in f]
        headers_list = main_list[0]
        values_list = main_list[1: len(main_list)]
        ready_list = []
        for string in range(string_quantity - 1):
            dict_ = {headers_list[header]: values_list[string][header] for header in range(len(headers_list))}
            ready_list.append(dict_)
    return ready_list


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
