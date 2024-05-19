#Задача «Сдача всем»

name = input('Название товара: ')
price = int(input("Цена в руб.: "))
weight = int(input("Масса в кг: "))
money = int(input())
change = int(money - weight * price)

print(f" Чек: {name} - {weight}кг - {price}руб/кг")

print(f"Итого: {weight * price}руб")

print(f"Внесено: {money}руб")

print(f"Сдача: {change}руб")