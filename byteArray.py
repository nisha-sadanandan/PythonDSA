# python byte array gives a mutable sequence of integer in the range 0<=x<256

#creating bytearray
a = bytearray((12, 8, 25, 2))
print("creating bytearray:")
print(a)

#accessing element
print("\n accessing element:",a[1])

#modifing element
a[1] = 3
print("\n after modifying:")
print(a)

#append element
a.append(30)
print("\nafter adding element:")
print(a)