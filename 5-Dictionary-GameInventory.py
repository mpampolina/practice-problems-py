def add_to_invent(inventory, loot):
    for items in loot:
        inventory.setdefault(items, 0)
        inventory[items] = inventory[items] + 1


def display_invent(inventory):
    print('Inventory:')
    tot_item = 0
    for items, quantity in inventory.items():
        print(items + ':', quantity)
        tot_item = tot_item + quantity
    print('Number of item types in inventory: ' + str(len(inventory)))
    print('Number of total items in inventory: ' + str(tot_item))


Invent = {'arrow': 12, 'gold coin': 42, 'rope': 1, 'torch': 6, 'dagger': 1}
display_invent(Invent)

print('\n\n')
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
add_to_invent(Invent, dragonLoot)

display_invent(Invent)
