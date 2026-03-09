colleceted_numbers=[]
while True:
    try:
        number=int(input("Enter a Number: "))
    except ValueError:
        print("Input is Invalid")
        break
    if number not in colleceted_numbers:
        colleceted_numbers.append(number)
        colleceted_numbers.sort()
    print("Lowest number is:",colleceted_numbers[0])
    print("Current list of Numbers:",colleceted_numbers)