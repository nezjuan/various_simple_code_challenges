stored_numbers=[]
while True:
    try:
        number=int(input("Enter a Number: "))
        stored_numbers.append(number)
        stored_numbers.sort(reverse=True)
        print("Current List of Numbers:",stored_numbers)
    except ValueError:
        print("Input is Invalid")
        break