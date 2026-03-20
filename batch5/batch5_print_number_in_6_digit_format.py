digit=input("Enter a number ranging from 0-1000:",)
six_digit = digit.zfill(6)
six_dig_form = [int(ch) for ch in six_digit]
print("Output:", six_digit)