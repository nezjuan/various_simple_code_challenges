user_name=input("Please Enter Full Name with improper casing:",)
pascal_cased=''.join(word.capitalize() for word in user_name.split())
print("Pascal Cased:",pascal_cased)