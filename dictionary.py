# python dictionary is an ordered collection of data that store data in format of key value pair.
#indexing of a python dictionary is done with the help of keys.
#these are of any hashable type ie,an object whose can never change like strings,numbers,tuples.
#we can create dictionary using curly braces or dictionary comprehention


#creating a dictionary

Dict = {"name":"navi",1:[1,2,3,4]}
print(Dict)

#accessing element using key
print("accessing element using key: ")
print(Dict[1])
print(Dict["name"])

#accessing elemnt using get
print("accessing element using get:")
print(Dict.get(1))
print(Dict.get("name"))

#creation using dictionary comprehention
myDict = {x: x**2 for x in [1,4,7,8,9]}
print(myDict)