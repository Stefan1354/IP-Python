#1.Напишете програма, в която потребителя въвежда неограничен брой цели числа от клавиатурата, за край на въвеждането
#се приема 0 (нула). Да се създадът два списъка:
   # - в първият списък да се запишат тези числа от въведените от потребителя, които са кратни на 3 и са четни. Намерете
   #сумата на елементите от списъка, чиито индекси са нечетни.
   # - Във втория списък да се запишат тези числа от въведените от потребителя, които са кратни на 7 и са нечетни. Сортирайте
   #списъка в низходящ ред. Намерете произведението на елемента с минимална и елемента с максимална стойност от този списък.

l = []

while True:
    s = int(input("Enter number "))
    if s != 0:
        l.append(s)
    else:
        break

l1 = []
l2 = []
for item in l:
    if item % 3 == 0 and item % 2 == 0:
        l1.append(item)
    elif item % 7 == 0 and item % 2 != 0:
        l2.append(item)
print(f"l1 = {l1}")
l2.sort(reverse=True)
print(f"l2 = {l2}")

s = 0
for i in range(len(l1)):
    if i % 2 != 0:
        s += l1[i]
print(f"sum of elements with odd indexes = {s}")

l2_min = min(l2)
l2_max = max(l2)

M = l2_min  * l2_max
print(f"l2_min * l2_max = {l2_min} * {l2_max} = {M}")


#2.Да се състави програма на Python за количка на електронен магазин с включени продукти: Рутер Xiaomi Mi Router 4C,
#Рутер Xiaomi Router 4A, Рутер TP-Link Archer C54 AC 1200, Рутер TP-Link Archer C80 AC1900 с полета: производител, 
#код на продукта, единична цена, количество. Да се състави:
#метод за добавяне на нови продукти в количката
#метод за извеждане на крайната цена за запплащане с включено ДДС и цена на доставка в текстов файл.

class Router:
    def __init__(self, brand, model, price, quantity):
        self.brand = brand
        self.model = model
        self.price = price
        self.quantity = quantity

class Cart:
    def __init__(self):
        self.cart = []

    def add_to_cart(self, model, brand, price, quantity):
        router_to_add = Router(model=model, brand=brand, price=price, quantity=quantity)
        self.cart.append(router_to_add)

    def write_price(self):
        total_price = 0
        for item in self.cart:
            total_price += item.price * item.quantity
        price_with_tax = total_price + total_price * 1 / 5
        price_with_delivery = price_with_tax + 3

        print(f"Price = {total_price}")
        print(f"Price (with tax)= {price_with_tax}")

        with open("price.txt", 'w') as file:
            str_to_write = f"Total price = {total_price} \n" \
                           f"Price (with tax) = {price_with_tax} \n" \
                           f"Price (with delivery) = {price_with_delivery}"
            file.write(str_to_write)

cart = Cart()

cart.add_to_cart("Xiaomi", "Mi Router 4C", 20, 5)
cart.add_to_cart("Xiaomi", "Mi Router 4A", 20, 3)
cart.add_to_cart("TP Link", "Archer C54", 15, 3)
cart.add_to_cart("TP Link", "Archer C80 AC1900", 30, 2)

cart.write_price()
