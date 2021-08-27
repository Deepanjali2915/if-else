print("MAY I HELP YOU:.....")
print("WELCOME TO BANK WORLD:...")
print("PLEASE SWIP YOUR CARD:...")
transction=("balance enquiry, Withrow money, Depisit, Change  your pin, Transfer money,Quit:...")
atmpin=1529
pin= int(input("ENTER YOUR 4 DIGIT PIN NUMBER:......."))
if pin!=atmpin:
    print("Ooops... Wrong password:...")
elif pin==atmpin:    
    print("CHOICE YOUR PIN TO PROCEED:") 
    print("Balance Enquiry:1:")
    print("Deposit money:2:")
    print("Change your pin:3:")
    print("Transfer money:4:")   
    print("Quit:5:") 
    Trans=(input("transctions"))
    if Trans=="Balance Enquiry" or "1":
        amt=56790
        BALANCE=(input("ENTER PLEASE:...."))
        if BALANCE=="amt":
            print("your balance",amt)
        else:
            print("No balance;.....")    
    elif Trans=="Deposit" or "3":
        Wbal=int(input("enter the amount:..."))
        if Wbal<=5000:
            print(Wbal,"Deposit successfully")
        else:
            print("Not valid your entry:...")

    elif Trans=="hange your pin" or "4":
        Change =("enter your new pin:....")
        if Change>=0:
            print("Successfully change..")
        else:
            print("entry not valid")
    elif Trans=="Quit" or "5":
        quit=input("press the quit!..")
        if quit=="yes":
            print("Quit")
        else:
            "Choose any transcation please"          
else:
    print("Wrong pin, please try again:...")                  