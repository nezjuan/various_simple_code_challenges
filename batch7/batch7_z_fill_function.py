word=input("Enter a word/s: ")
width=int(input("Enter the total width: "))
sign=""
number_part=word
if word.startswith(("+","-")):
    sign=word[0]
    number_part=word[1:]
padding=width-(len(sign)+len(number_part))
if padding>0:
    result_string=sign+("0"*padding)+number_part
else:
    result_string=word
print("Z-Filled Output",result_string)