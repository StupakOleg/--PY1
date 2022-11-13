from pprint import pprint


numbers_list = [{'bin': bin(number), 'dec': number, 'hex': hex(number), 'oct': oct(number)} for number in range(16)]
pprint(numbers_list)
