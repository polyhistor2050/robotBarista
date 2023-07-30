print("Welcome to Fast Food Restaurant.")
price = 6
name = input("What is your name? ")
print("Hello " + name + " thank you so much for coming in today. \n")

menu = "Pizza, Noodles, Hotdogs, rameon, omlett"
print(name + " what would you like from our menu today? Here is what we are serving.\n" + menu)

order = input("Order your dish: \n")
totalOrder = input("How many " + order + " Would like to order: ")
totalCost = price * int(totalOrder)
print("Sounds good " + name + ", You ordered " + totalOrder + " " + order + " which cost " + str(totalCost) +  "$, We'll have your order ready for you in a moment.")
