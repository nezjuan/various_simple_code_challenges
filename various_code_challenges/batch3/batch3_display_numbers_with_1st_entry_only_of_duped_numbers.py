stored_numbers=[]
for numbers in range(10):
    number=int(input("Enter a Number: "))
    if number not in stored_numbers:
        stored_numbers.append(number)
print("The numbers are: ",stored_numbers)