#==================================================#
# Home Inventory Script -- homeinventory.py --
# C:\Users\Alleg\Python\UW Course\Week 3\homeinventory.py
# Assignment #3 - Create and Maintain External Inventory File
# DJP -- 2021-07-17 -- Initial script composition
#==================================================#
import json
######################################################################
# Title
print("\n\n================================")
print("==== Home Inventory Tracker ====")
print("================================")
######################################################################
# Open file handler
fhandle = open("homeinventory.json", "a")
######################################################################
# Get user input
while True:
    itemDict = {}
    item = input("\nEnter an item. || ").lower()
    print("")
    qty = int(input("How many? || "))
    print("")
    val = float(input(f"Enter the value of one '{item}'. || "))
    value = round(val, 2)

    print(f"\n|| {qty}x {item} @ ${value}/ea. ||\n")
    correct = input("Is this correct? ('Y'/'N')|| ").lower()
    print("")
####################
# Add input to JSON dictionary and append to file
    if correct == "n":
        continue
    elif correct != "y":
        print("\nInvalid input!")
        continue
    else:
        itemDict["item"] = item
        itemDict["quantity"] = qty
        itemDict["value-each"] = value
        js = json.dumps(itemDict, indent = 4)
        fhandle.write(js)
####################
# Rinse and repeat?
        more = input("Would you like to add another record? ('Y'/'N')|| ").lower()
        print("==================================================")
        if more == "y":
            print("")
            continue
        elif more == "n":
            print("\nProcessing complete!")
            break
        else:
            print("\nInvalid input!")
            continue
######################################################################
fhandle.close()

# homeinventory.py
