salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

# TODO Оформить решение
for month in range(10):
    prirost_in_month = ((1 + increase)**month)*spend - salary
    need_money += prirost_in_month
print(round(need_money))
