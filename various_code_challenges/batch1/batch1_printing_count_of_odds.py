odds=0
for n in range(10):
    number=int(input("Enter Number: "))
    if number%2!=0:
     odds+=1
print("Count of Odd Numbers:",odds)