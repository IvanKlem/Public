tikkets = int(input("Введите количество билетов: "))
if tikkets <= 0:
    tikkets = int(input("Количество билетов не может быть равно 0 или менее, введите верное количество: "))
i = 1
price = 0
while tikkets >= i:
    age = int(input("Введите возраст покупателя " + str(i) + "го билета: "))
    if 18 < age < 25:
        price += 990
    elif age > 25:
        price += 1390
    elif age < 18:
        print("Проход посетителя бесплатный!")
    i += 1
if tikkets > 3 and price != 0:
    dis = (price/100) * 10
    dis_price = price - dis
    print("Сумма к оплате: " + str(dis_price) + "\nУчтенная скида: " + str(dis))
elif price == 0:
    print("Оплата бителов не требуется")
else:
    print("Сумма к оплате: " + str(price))

