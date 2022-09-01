#1.Напишете програма в която потребителят въвежда n-брой цели числа от клавиатурата. Да се създадът два списъка - в 
#единия да се запишат всички нечетни числа, кратни на 3, а в другия всички четни числа, кратни на 2. За списъка, 
#съставен от нечетни числа, да се намери минималната и максималната стойност на елементите, съставящи списъка. 
#За списъка, съставен от четни числа, да се намери сумата и средно аритметичната стойност за елементите от списъка.

n = int(input("Enter n: "))
list_1 = []
list_2 = []
for i in range(n):
    num = int(input(f"Enter {i+1}.number "))
    if num%2!=0:
        if num%3==0:
            list_1.append(num)
    else:
        list_2.append(num)
print(list_1)
print(list_2)
print("Minimalnata stoinost na purviq spisuk e ", min(list_1))
print("Maksimalnata stoinost na purviq spisuk e ", max(list_1))
suma = 0
for i in list_2:
    suma+=i
print("Sumata na vtoriq spisuk e ", suma)
print("Srednoaritmeticnoto na vtoriq spisuk e ", suma/len(list_2))


#2. Да се състави програма на Python, която дефинира клас "GSM mobile devices",
#с полета: налично количество, единична цена, година на производство, 
#производител, модел на мобилни устройства. Да се състави:
#-метод, който сортира моделите мобилни устройства по налично количество
#в нарастващ ред;
#-метод, който премества всички модели мобилни устройства, произведени
#от един и същ производител в списък, записан в JSON файл.


import json

class GSM_mobile_devices:

    def __init__(self, qty, price, release_year, manufacturer, model):
        self.qty = qty
        self.price = price
        self.release_year = release_year
        self.manufacturer = manufacturer
        self.model = model
            
    def sort_by_qty(self):
        list_qty = []
        for phone in li:
            list_qty.append(phone.qty)
        list_qty.sort()
        
        for qty in list_qty:
            for item in li:
                if qty == item.qty:
                    print("Количество: %d  " % item.qty, "Модел: %s" % item.model, end = "\n")
                    
    def manufac_to_file(self):
        manufac = input("Enter a manufacturer: ")
        list_manufac = []
        for phone in li:
            if manufac == phone.manufacturer:
                list_manufac.append(phone.model)
        
        '''JSON'''
        f = open("file_phones.json", "w")
        f.write(json.dumps(list_manufac))
        f.close()
        return json.dumps(list_manufac)
        
        
GSM1 = GSM_mobile_devices(2,200,2020,"Nokia","g10")
GSM2 = GSM_mobile_devices(9,666,2022,"Iphone","Giga")
GSM3 = GSM_mobile_devices(1,1000,2022,"MyPhone","BETA")
GSM4 = GSM_mobile_devices(0,99,2016,"MyPhone","a2200")
GSM5 = GSM_mobile_devices(6,300,2020,"Nokia","SmartS")
GSM6 = GSM_mobile_devices(3,662,2020,"Nokia","XYZ")

li = [GSM1,GSM2,GSM3,GSM4,GSM5,GSM6]
GSM1.sort_by_qty()
print(GSM1.manufac_to_file())
