import time

print("To play this game you may need some instructions.")
print("You will be asked questions and given responces to choose from.")
print("Type your responce then hit enter.")
print("To check your inventory type inventory and to drop an item type the item number.")
print("To use an item type use /Item name/")

start = (input("Enter start to start game.\n\n"))
Q1 = input("zzzzz...\n\nWAKE UP!!!\n\nA. WHAT HAPPENED?!\nB. 5 more minuets.\n\n")

if start == True:
    print(Q1)
    if Q1 == "A":
        print("explanaitionsjgfh")
    if Q1 == "B":
        print("FINE")
        time.sleep(300)
        print(Q1)

        
if start == "start":
    start == True
else:
    start == False
    print("start")


