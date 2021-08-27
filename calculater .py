a =int(input("enter the number 1..."))
b =int(input("enter the number 2..."))
c =input("enter the operator")
if c=="+":
    print(a+b)
elif c=="-":  
    print(a-b) 
elif c=="*":   
    print(a*b)
elif c=="%":
    print(a%b)
elif c=="/":
    print(a/b)
elif c=="//":
    print(a//b)
elif c=="**":
    print(a**b)
else:
    print("not valid")        