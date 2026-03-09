no1=int(input("Enter First Number: "))
no2=int(input("Enter Second Number: "))
in_between_no=[]
while no1<no2-1:
    no1+=1
    in_between_no.append(no1)
print("The numbers between",no1-len(in_between_no),"to",no2,"are:",in_between_no)