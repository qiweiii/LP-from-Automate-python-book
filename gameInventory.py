# Game inventory

# inventory.py
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        # FILL IN THE CODE HERE
        item_total += v
        print(str(v) + ' ' + k)
    print("Total number of items: " + str(item_total))

displayInventory(stuff)

# Another function...
print("-------------------------")

def addToInventory(inventory, addedItems):
    # your code goes here
    for items in addedItems:
        inventory.setdefault(items, 0)
    for i in inventory.keys():
        for x in addedItems:
            if i == x:
                inventory[i] += 1

    return inventory
        

inv = {'gold coin': 42, 'rope': 1}

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
