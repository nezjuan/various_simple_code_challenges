colleceted_numbers=[]
while True:
    try:
        number=int(input("Enter a Number: "))
    except ValueError:
        print("Invalid Input")
        break
    if number not in colleceted_numbers:
        colleceted_numbers.append(number)
        print("This number is UNIQUE\n""Current Numbers:",colleceted_numbers)
    elif number in colleceted_numbers:
        print("This number is a DUPLICATE")