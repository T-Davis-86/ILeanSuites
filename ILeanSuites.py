#Declaring variables
beds = 0
fee = 0
sb = 0
db = 0 
tax = 0
subtot = 0
total = 0
price = 0
room_num = 0
rooms = 0
smokey = 0
#Using a while loop to allow the program to run 10 times
while rooms != 10:
    print("============================================")
    print("Hello, welcome to I Lean Suites!")#I Lean is joke on myself since I only have one leg I tend to lean to one side. lol
    #display rates:
    print("Room with Double beds: $50 per room")
    print("Room with Single bed: $20 per room")
    print("Smoking room fee $20 per room")
    print("More than 2 people to room fee: $40 per room")
    print("============================================")
    print("!!!!!Verify Caps lock on!!!!!")
    name = input("Name on the reservation? Type your name how you would like it to appear on invoice.\n")#Taking information for the invoice
    ppl = int(input("How many occupants per room?\n"))#This to determine how many people are staying in each room
    global room
    room = int(input("How many rooms would you like?\n"))#This is to determine how many rooms to charge the client
    nights = int(input("How many nights will you be staying with us?\n"))#This information is used to charge client
    exempt = input("Are you tax exempt? Type Yes or No\n")#Used to determine whether the client is to be taxed
    def main():#print Invoice to text file
        f=open ("I Lean Suites Invoice.txt","w+")#Creating a text file to store the INVOICE
        for i in range (1):
            f.write("=============================INVOICE===============================\n")#Writing in the text file created for the INVOICE
            f.write("Name:"+str(name)+"\n")#Information for the INVOICE after Converting int into strings
            f.write("-------------------------------------------------------------------\n")
            f.write("You're booked for: "+str(room)+" Room(s), with "+str(ppl)+" occupants:\n")#Information for the INVOICE after Converting int into strings
            f.write("\n")
            f.write("Charge................................................$ "+str("{0:.2f}" .format(fee))+"\n")#Information for the INVOICE
            f.write("-------------------------------------------------------------------\n")
            f.write("\n")
            f.write("Your rooms will have "+str(db)+" Double Beds & "+str(sb)+" Single beds\n")#Information for the INVOICE after Converting int into strings
            f.write("\n")
            f.write("Charge................................................$ "+str("{0:.2f}" .format(sleep))+"\n")#Information for the INVOICE
            f.write("-------------------------------------------------------------------\n")
            f.write("\n")
            if room > 1:
                f.write(str(smokey)+" of the "+str(room)+" room(s) are smoking rooms.\n")#Information for the INVOICE after Converting int into strings
                f.write("\n")
                f.write("Charge..................................................$  "+str("{0:.2f}" .format(price))+"\n")#INVOICE information
            else:
                f.write("Your rooms is booked as "+str(smokey)+" room\n") #Information for INVOICE if only one room is selected
                f.write("\n")
                f.write("Charge...................................................$  "+str("{0:.2f}" .format(price))+"\n") #INVOICE information
            f.write("-------------------------------------------------------------------\n")
            f.write("\n")
            f.write("Your registering as "+str(exe)+" for taxes.\n")#Information for the INVOICE after Converting int into strings
            f.write("\n")
            f.write("Charge...................................................$  "+str("{0:.2f}" .format(tax))+ "\n") #INVOICE information
            f.write("===================================================================\n")#Information for the INVOICE after Converting int into strings
            f.write("Single night subtotal:...................................$ "+str("{0:.2f}" .format(ssub))+ "\n")#Information for the INVOICE after Converting int into strings
            f.write("single night total with tax:.............................$ "+str("{0:.2f}" .format(stot))+ "\n")#Information for the INVOICE after Converting int into strings
            f.write("===================================================================\n")#Information for the INVOICE after Converting int into strings
            f.write("You're booked for: "+str(nights)+" Night(s):\n")#Information for the INVOICE after Converting int into strings
            f.write("---------------------------------------------------------\n")            
            f.write("Booked for " + str(nights) + " nights subtotal:........................... $ "+str("{0:.2f}" .format(subtot))+"\n")#Information for the INVOICE after Converting int into strings
            f.write("Booked for " + str(nights) + " nights total:.............................. $ "+str("{0:.2f}" .format(total))+"\n")#Information for the INVOICE after Converting int into strings
            f.write("==================================================================\n")#Information for the INVOICE after Converting int into strings
        f.close()#Closing the text file that was created
    def smokies():#this function is used to when there are multiple rooms that are going to be smoking
        global smokey
        smokey = int(input("How many rooms will be smoking rooms?\n"))
        global price
        price = smokey * 20    
    def beddy():#This function is used when multiple rooms are rented but all rooms will have the same amount of beds
        b = input("All rooms will have Double or Single bed? Type Single or Double\n")
        if b == "DOUBLE":
            beds = 50
            global db
            db = 1
        elif b == "SINGLE":
            beds = 20
            global sb
            sb = 1
        global sleep
        sleep = beds * room #This calculation is used to determine what is being charged when all beds are the same
    def bedding():#this function is for when there are multiple rooms but with different amount of beds
        global db
        db = int(input("How many rooms with Double beds?\n"))
        beds = 50 * db
        global sb
        sb = int(input("How many rooms with Single beds?\n"))
        sbs = sb * 20
        global sleep
        sleep = beds + sbs#calculation used to charge for different amount of beds
    def multi():#this function is used for when there are multiple rooms being rented
        bed = input("Will rooms have different amount beds? Type Yes or No\n")
        if bed == "YES":
            bedding()#function for multiple rooms with different bed amounts
        else:
            beddy()#function for mutiple rooms with same bed amounts
        if ppl >= 3:
            global fee
            fee = 40 * room#calculatation for amount of people per a room
        else:
            fee = 20 * room#calculation for amount of people per a room
        smoke = input("Will any of these rooms being a Smoking room(s)? Type Yes or No\n")
        if smoke == "YES":
            smokies()#function used to calculate how many rooms will be smoking
        elif smoke == "NO":
            global smokey
            smokey = 0
            global price
            price = 00.00#calculation for rooms that are Non-smoking
        if exempt == "NO":#used to determine whether tax is applied
            global tax
            tax = 00.07
            global exe
            exe = "Non-Exempt"
        else:
            tax = 00.00
            exe = "Exempt"
    def single():#function for a single room being rented
        bed = input("Would you like a Single or Double bed? Type Single or Double\n")#Determining amount of beds for room rented
        if bed == "DOUBLE":#Determining charge for amount of beds
            beds = 50
            global db
            db = 1
        elif bed == "SINGLE":
            beds = 20
            global sb
            sb = 1
        global sleep
        sleep = beds * room#Calculation for amount of beds per room
        if ppl >= 3:#Calculating what to charge per occupants per room
            global fee
            fee = 40
        else:
            fee = 20
        global smokey
        smokey = input("Smoking or Non-Smoking? Type Smoking or Non-Smoking\n")#Determining if single room is smoking or non-smoking
        if smokey == "SMOKING":#Used for calculating price for smoking room
            global price
            price = 20
        else:
            price = 0
        if exempt == "NO":#Deteremining if tax is applied
            global tax
            tax = 00.07
            global exe
            exe = "Non-Exempt"
        else:
            tax = 00.00
            exe = "Exempt"
    if room > 1:
        multi()#function used when more than 1 room is being rented
    else:
        single()#function used when only a single room is rented
    ssub = (sleep+fee+price)
    stot = (ssub * tax) + ssub
    subtot = (sleep+fee+price) * nights#calculating the subtot of everything being charged
    total = (subtot * tax) + subtot#total calculation of everything being charged including tax if applicable
    print("======================INVOICE======================\n")#Created for the on screen INVOICE
    print("Name:",(name)+"\n")#Information for the on screen INVOICE
    print("You're booked for:",(nights),"Night(s)\n")#Information for the on screen INVOICE
    print("You're booked for:",(room),"Room(s)\n")#Information for the on screen INVOICE
    print("Your rooms will have",(db),"Double Beds &",(sb),"Single beds\n")#Information for the on screen INVOICE
    if room > 1:
        print((smokey),"of the",(room),"room(s) are smoking rooms.\n")#Information for the on screen INVOICE after Converting int into strings
    else:
        print("Your rooms is booked as",(smokey),"room\n") #Information for on screen INVOICE if only one room is selected
    print("Your registering as",(exe),"for taxes.\n")#Information for the on screen INVOICE
    print("Your subtotal: $",("{0:.2f}" .format(subtot))+"\n")#Information for the on screen INVOICE
    print("Your total with tax: $",("{0:.2f}" .format(total))+"\n")#Information for the on screen INVOICE
    print("===================================================\n")#Information for the on screen INVOICE
#printing the invoice on whats being charged
    main()
    rooms += room
    next = input("Press Enter For Next Reservation")
    if rooms >= 10:#Used to stop the loop when cycled 10 times
        break
