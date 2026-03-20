user_name=input("Please Enter Full Name with improper casing:",)
snake_cased='_'.join(word.lower() for word in user_name.split())
print("Snake Cased:",snake_cased)