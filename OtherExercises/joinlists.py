list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3) #['a','b','c',1,2,3]

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1) #['a','b','c',1,2,3]

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1) #['a','b','c',1,2,3]

fruits=["apple","banana",'cherry']
for x in fruits:
      if x=="banana":
            continue
      print(x)  #apple
                #cherry
print(x) #cherry

fruits=["apple","banana","cherry"]
for x in fruits:
  if x=="banana":
    break
  print(x) #apple
print(x) #banana

fruits={"apple","banana","lemon"}
more_fruits=["orange","mango","waterlemon"]
fruits.update(more_fruits)
print(fruits) #printira sve zaedno {'apple','mango,...'banana'}

fruits={'apple','banana','mango'}
fruits.discard('banana')
print(fruits) #{'apple','mango'}

car={
  "brand":"Ford",
  "model":"Mustang",
  "year": 1964
}
print(car.get("model")) #Mustang

car={
  "brand":"Ford",
  "model":"Mustang",
  "year": 1964
}
car["year"]=2020 #menjame godinata
print(car)

car={
  "brand":"Ford",
  "model":"Mustang",
  "year": 1964
}
car["color"]="red"
print(car) #dodava u recniko color:red

car={
  "brand":"Ford",
  "model":"Mustang",
  "year": 1964
}
car.pop("model")
print(car)  #brise model

car={
  "brand":"Ford",
  "model":"Mustang",
  "year": 1964
}
car.clear()
print(car)
