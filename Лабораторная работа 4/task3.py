def delete(list_, index=None):
    length = len(list_)
    if index is not None:
        ready_list = list_[:index] + list_[index + 1:]
        return ready_list
    else:
        ready_list = list_[:length - 1]
        return ready_list


print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
