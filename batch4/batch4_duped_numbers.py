stored_numbers=[]
dupes=[]
for numbers in range(10):
    number=int(input("Enter a Number: "))
    if number in stored_numbers and number not in dupes:
        dupes.append(number)
    else:
        stored_numbers.append(number)
print("The duplicated numbers are:",dupes)