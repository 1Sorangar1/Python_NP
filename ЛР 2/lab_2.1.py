money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
current_money = money_capital-spend
month = 1
while current_money > 0:
    spend *= (1+increase)
    current_money += salary-spend
    month += 1

print("Количество месяцев, которое можно протянуть без долгов:", month)
