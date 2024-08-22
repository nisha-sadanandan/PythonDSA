#tuples are similar to list but tuples are immutable in nature.Tuple items are ordered, unchangeable, and allow duplicate values.
#once it is created it cannot be modified.just like list ,a tuple also contain element of various type


#creating tuple using the strings

Tuples = ("this", "is", "good")
print("\n tuples with the use of string:")
print(Tuples)

#creating tuple with the use of list:
List = [1, 2, 5,"naveen",6]
print("\ntuples using the list:")
Tuple = tuple(List)
print(Tuple)

#accessing elemnt using indexing
print("\n first element of tuple")
print(Tuple[0])

#accessing last element using indexing
print("\nlast element of tuple")
print(Tuples[-1])
