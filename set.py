#set is a mutable collcetion of data does n0t allow any duplicattion ,
#the data structure used inthis is Hashing ,a popular techniqe to perform insertion,deletion,and traversal in on average
#if multiple values are presnt in same index position .then the value is append to that index positionto form a linked list



#creating a set with mixed type of values
Set = set([1, 2, 3, "neethu", 4, 5,])
print("\n set with use of mixed values")
print(Set)

#accessing element using loop
print("\n element of the set")
for i in Set:
    print(i,end=" ")

print()    

print("nisha" in Set)