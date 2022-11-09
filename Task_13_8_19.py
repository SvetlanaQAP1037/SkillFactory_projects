from decimal import Decimal
tickets = int(input("Введите количество билетов, которые хотите приобрести: "))
list_of_visitors = []
cost_of_tickets = {'up_to_18': 0, 'from 18 to 25': 990, 'from 25': 1390}
total = []
count = 0
while count != tickets:
    age = int(input("Введите возраст посетителя: "))
    list_of_visitors.append(age)
    count += 1
    if age < 18:
       total.append(cost_of_tickets.get('up_to_18')),
    elif 18 <= age < 25:
        total.append(cost_of_tickets.get('from 18 to 25')),
    elif age >= 25:
        total.append(cost_of_tickets.get('from 25')),
# print('Возраст посетителей:', list_of_visitors)
# print('Стоимость за каждый билет:', total)
print('Сумма оплаты в руб.:', Decimal(sum(total)).quantize(Decimal("1.00")))
for customers in list_of_visitors:
    if len(list_of_visitors) >= 3 and sum(total) > 0:
        print("Вы зарегистрировали 3-х человек (или более), получаете скидку '10%'")
        print('Сумма оплаты в руб. с учетом скидки "10%":',
              Decimal((sum(total) - sum(total) / 10)).quantize(Decimal("1.00")))
        break