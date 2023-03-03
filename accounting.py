def automa(name,m,p):
    #converts to float
    melons = float(m)
    #converts to float
    paid=float(p)
    #constant price
    MELON_COST = 1.00
    #gets total price
    expected_amount = MELON_COST * melons
     #If customer overpaid, print that they've overpaid for their melons. If
     # customer underpaid, print that they've underpaid for their melons.
    if expected_amount > paid:
        print(f"{name} paid ${paid:.2f},",f"expected ${expected_amount:.2f}" )
        print(f"{name} underpay ${expected_amount - paid:.2f}")
    elif expected_amount == paid:
        print(f"{name} paid ${paid:.2f},",f"expected ${expected_amount:.2f}" )
        print(f"{name} paid the right amount ${expected_amount:.2f}.")
    else:
        print(f"{name} paid ${paid:.2f},",f"expected ${expected_amount:.2f}" )
        print(f"{name} overpaid ${paid - expected_amount:.2f}")

   

#opens the file
file_text = open("customer-orders.txt")
#It intitates through every line
for file in file_text:
    #converts it into a list of strings
    file = file.rstrip().split("|")
    # calls functionm with name,amount and paid arguments
    automa(file[1],file[2], file[3])
    # closes file
file_text.close()






