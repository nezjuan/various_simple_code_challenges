colleceted_numbers=[]
while True:
    number=int(input("Enter a Number: "))
    if number not in colleceted_numbers:
        colleceted_numbers.append(number)
        colleceted_numbers.sort()
    print("Lowest number is:",colleceted_numbers[0])
    print("Current list of Numbers:",colleceted_numbers)