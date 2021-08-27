day = input("Aaj ka din kya hai? (monday/tuesday) > ")
time = input("Kaunse samay ka khana banana hai? (lunch/dinner) > ")
if day == "monday/tuesday" or time == "lunch/dinner":
     print ("Daal-Roti banegi aaj")
elif day == "tuesday" and time == "dinner":
    print ("Pav-Bhaji banegi aaj toh ")
elif day == "tuesday" and time == "lunch":
    print("Daal-Roti banegi aaj") 
      