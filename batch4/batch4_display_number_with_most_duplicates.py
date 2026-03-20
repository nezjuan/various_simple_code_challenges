stored_numbers=[]
duped_numbers=[]
while True:
    try:
        number=int(input("Enter a Number: "))
        if number not in stored_numbers:
            stored_numbers.append(number)
        elif number in stored_numbers:
            duped_numbers.append(number)
    except ValueError:
        print("Invalid input")
        break
    print("The duplicated numbers are:",duped_numbers)
    print("The current numbers are: ",stored_numbers)
    if duped_numbers:
        most_dup = max(duped_numbers, key=duped_numbers.count)
        print(f"The number with the most duplicates is: {most_dup} (appeared {duped_numbers.count(most_dup)} times)")
    else:
        print("No duplicates found.")