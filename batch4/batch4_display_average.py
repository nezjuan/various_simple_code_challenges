stored_numbers=[]
stored_numbers_count=0
total=0
while True:
    try:
        number=int(input("Enter a Number: "))
        stored_numbers.append(number)
        stored_numbers_count+=1
        total+=number
        average=total//stored_numbers_count
        print("Average of given numbers:",average)
        print("Current List of Numbers:",stored_numbers)
    except ValueError:
        print("Input is Invalid")
        break