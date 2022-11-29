
import coffee as cf

print(f"Welcome to {cf.shop_name}")
print(f"Available sizes: {cf.coffee_sizes}")
print(f"Available roasts: {cf.coffee_roasts}")


size = input("Coffee size: ")
roast = input("Type of roast: ")

order = cf.order_coffee(size, roast)

milk_option = input("Do you want milk (Y/N): ")

if "y" in milk_option.lower():

    milk_amount = input("How much milk in %: ")

    milk_added = cf.add_milk(milk_amount)

    print(order)
    print(milk_added)
    
else:
    print(order)


print("That's pretty good")
print("I should probably give a tip... let's see.")

tip_option = input("Do you want to give a tip? (Y/N): ")

if "y" in tip_option.lower():
    tip_amount = input("How much tip should it be: ")
    tip_given = cf.give_tip(tip_amount)

    print(tip_given)
else:
    print("I have no money to spare this time around...")

