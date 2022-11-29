def add_fruit(inventory, fruit, quantity=0):
    
    if fruit in inventory:
        inventory[fruit] += quantity
    else:
        inventory[fruit] = quantity


# make these tests work...
new_inventory = {}
add_fruit(new_inventory, 'strawberries', 10)
print(new_inventory)
#  test that 'strawberries' in new_inventory
#  test that new_inventory['strawberries'] is 10
add_fruit(new_inventory, 'strawberries', 25)
print(new_inventory)
#  test that new_inventory['strawberries'] is now 35)
