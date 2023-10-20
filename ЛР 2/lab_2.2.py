salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = spend-salary
months_current = months - 1
while months_current > 0:
    spend *= (1+increase)
    money_capital += spend-salary
    months_current -= 1

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))
