print("HOW TO EXCHANGE 2 NUMBERS USING TEMPORARY VARIABLES")
a=int(input("ENTER a Number"))
b=int(input("Enter the second number"))
print("The number before exchange are a",a,"b",b)
print("After exchange")
a=a+b
b=a-b
a=a-b
print("new valuues are a=",a,"b=",b)