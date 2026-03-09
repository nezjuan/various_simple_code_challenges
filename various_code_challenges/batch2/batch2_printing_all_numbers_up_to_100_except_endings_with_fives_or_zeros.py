for numbers in range(1,101):
    numbers=str(numbers)
    if numbers[-1]!="0" and numbers[-1]!="5":
        numbers=int(numbers)
        print(numbers)