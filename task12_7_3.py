from decimal import Decimal

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money = float(input("Введите сумму, которую хотите положить на годовой вклад: "))
bank_tkb = Decimal(money / 100 * per_cent['ТКБ']).quantize(Decimal("1.00"))
bank_skb = Decimal(money / 100 * per_cent['СКБ']).quantize(Decimal("1.00"))
bank_vtb = Decimal(money / 100 * per_cent['ВТБ']).quantize(Decimal("1.00"))
bank_sber = Decimal(money / 100 * per_cent['СБЕР']).quantize(Decimal("1.00"))

deposit = [bank_tkb, bank_skb, bank_vtb, bank_sber]
print(list(map(str, deposit)))
print("Максимальная сумма, которую вы можете заработать - ", max(deposit))








