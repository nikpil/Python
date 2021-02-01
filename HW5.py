proceed = int(input('Введите выручку '))
costs = int(input('Укажите издержки '))

if proceed > costs:
    print('Вы в прибыли')
else:
    print('У вас убыток')

if proceed > costs:
    profit = (proceed - costs)
    profitability = int(profit / proceed * 100)
    print("Ренабельность =", profitability, "%")

staff = int(input("Введите количество сотрудников "))
profit_staff = profit / staff
print("Прибыль на одного сотрудника =", profit_staff)
