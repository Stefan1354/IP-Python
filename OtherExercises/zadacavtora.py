import json

class GSM_Mobile_Devices:
    def __init__(self, quantity, price, year, make, model):
        self.quantity=quantity
        self.price=price
        self.year=year
        self.make=make
        self.model=model

    def __str__(self):
        return f"{self.make} model {self.model} price {self.price} and {self.quantity} quantity"
    
gsm=[GSM_Mobile_Devices(45, 100, 2010, 'Nokia', '3310'),
     GSM_Mobile_Devices(20, 400, 2012, 'Ihphone', '11 Pro'),
     GSM_Mobile_Devices(30, 150, 2015, 'Nokia', '5410'),
     GSM_Mobile_Devices(15, 200, 2021, 'Nokia', "6300")]

def sort_gsm(gsm_list):
    gsm_list.sort(key=lambda x : x.quantity)

    for obj in gsm:
        print(obj)

def find_model(make, gsn_list):
    same_make=[]
    for obj in gsn_list:
        if obj.make==make:
            same_make.append(obj.model)

    for obj in same_make:
        print(obj)
    
    f=open("file_phones.json", "a")
    f.write(json.dumps(same_make))
    f.close()
    #return json.dumps(same_make)
    #json_string=json.dumps(same_make)
    #return json_string

print('\n---sortirani---')
sort_gsm(gsm)

print('\n---ist proizvoditel---')
find_model('Nokia',gsm)