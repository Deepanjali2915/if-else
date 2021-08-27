number=int(input("ENTER THE NUMBER"))
if number%3==0 and number%7==0:
    print("navgurukul") 
elif number%7==0:
    print("nav")
elif number%3==0:
    print("gurukul")    
else:
    print("not valid number")       
