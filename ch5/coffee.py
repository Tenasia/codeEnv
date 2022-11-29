""" 

The coffee shop module contains functions and variables 
important to implementing a coffee shop

"""


shop_name = "Runestone Brew House"
coffee_sizes = ["small", "medium", "large"]
coffee_roasts = ["hot chocolate", "light", "medium", "dark", "espresso"]


def order_coffee(size, roast):
    
    if size in coffee_sizes and roast in coffee_roasts:
        pass
    else:
        print("Not a valid coffee size or roast")
        exit()
    
    return f"Here's your {size} coffee roasted {roast}"

def add_milk(fat_content):

    fat_content = int(fat_content)

    return f"I've added {fat_content}% milk to your coffee."

def give_tip(tip_amount):

    tip_amount = int(tip_amount)
    return f"Thank you so much!"