#Dictionary
print('#Update')
thisdict={"model":"model x","year":1984,"date":14/2}
print(thisdict)
print(thisdict["model"])
print(thisdict.get("model"))
thisdict["year"]=2020
print(thisdict)

#deleting last item

#Access
thisdict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict1.update({"year": 2020})
print(thisdict1)

print('#Check')
car={"brand":"Ford", "model":"model x", "colour":"White"}
if "year" in car:
    print("yes")
else:
    car["brand"]="Ferrari"
    print(car)

print('#Keys')
car={"brand":"Ford", "model":"model x", "colour":"White"}
print(car)
x=car.keys()
print(x)
print(car.values())
print(car.items())
car["model"]="model sexy"
car["colour"]="Blue"
print(car)

print('#Loop')
car={"brand":"Ford", "model":"model x", "colour":"White"}
for x,y in car.items():
  print(x,y)
if "Ford" in y:
  print("yes")

print('#Looping loop')
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
if "name" in child1:
    print("yes")
print(myfamily["child2"]["name"])

