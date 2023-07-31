print("Welcome to Fast Food Restaurant.")
price = 6
name = input("What is your name? ")
if name == "Ben":
    print("Your not welcome here evil ben")
    exit()
else:
    print("Hello " + name + " thank you so much for coming in today. \n")

    menu = "pizza, noodles, hotdogs, rameon, omlett"
    print(name + " what would you like from our menu today? Here is what we are serving.\n" + menu)
    
    order = input("Order your dish: \n")
    if order == "pizza":
        price = 25
    elif order == "noodles":
        price = 3
    elif order == "omlett":
        price = 9
    elif order == "hotdogs":
        price = 6
    elif order == "rameon":
        price = 6
    else:
        print("We don't have that here")
        exit()
        
    totalOrder = input("How many " + order + " Would like to order: ")
    totalCost = price * int(totalOrder)
    print("Sounds good " + name + ", You ordered " + totalOrder + " " + order + " which cost " + str(totalCost) +  "$, We'll have your order ready for you in a moment.")
