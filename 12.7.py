per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("введите сумму: "))
deposit = []
deposit.append(int(money/100*per_cent['ТКБ']))
deposit.append(int(money/100*per_cent['СКБ']))
deposit.append(int(money/100*per_cent['ВТБ']))
deposit.append(int(money/100*per_cent['СБЕР']))
print(deposit)
deposit.sort(reverse=True) #обратная сортировка списка от большего к меньшему
print("Максимальная сумма, которую вы можете заработать", deposit[0])
# max(deposit) - максимальное значение списка можно так же получить черех функцию max