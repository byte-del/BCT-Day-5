x=int(input("Enter the first number: "))
y=int(input("Enter the second number: "))
try:
    z=x/y
    print("Divison result = ",z)
except Exception as e:
    print(e)
print("Hello this line is last line")