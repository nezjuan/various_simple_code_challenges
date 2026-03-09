subtractor=int(input("Enter First Number: "))
next_9_numbers=[]
for n in range(9):
    next_9_numbers.append(int(input("Enter Next Numbers: ")))
for numbers in next_9_numbers:
    subtractor-=numbers
print("Result is: ",subtractor)