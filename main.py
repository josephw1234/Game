# Joseph Woodward
# CS 30
# Period 1 Quint 1
# Sept 18 2020
# Numerical RPG inventory list


weapons = ["Sword", "Axe", "Bow", "Arrows"]
armour = ["Chestplate", "Gloves", "Boots", "Helmet"]
consumables = ["Potion", "Bread", "First aid kit"]

# Prints list of weapons
print("Available weapons:")
for item in weapons:
    index = weapons.index(item)
    print(str(index + 1) + ". " + str(item))

# Prints list of armour
print("\nAvailable armour:")
for item in armour:
    index = armour.index(item)
    print(str(index + 1) + ". " + str(item))

# Prints list of consumables
print("\nAvailable consumables:")
for item in consumables:
    index = consumables.index(item)
    print(str(index + 1) + ". " + str(item))
