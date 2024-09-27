inventory = [
    ["sunsilk", 5, 5],
    ["piattos", 10, 15],
    ["manga", 15, 5],
    ["oishi", 10, 7],
    ["fita", 8, 10],
]  # initalized list with values
while True:  # looping until user enter 6 to exit
    print("Inventory System!")
    print("[1].Add an item to the inventory (name, quantity, price).")
    print("[2].Remove an item by name.")
    print("[3].Update item quantity when stock is added or sold.")
    print("[4].Display all items in the inventory.")
    print("[5].Search for an item by name.")
    print("[6].Exit")
    choi = int(input("Enter your choice: "))
    # Add items in list
    if choi == 1:
        name = input("Enter name: ")
        quantity = int(input("Enter quantity: "))
        price = int(input("Enter price: "))
        # using append to add in list
        inventory.append([name, quantity, price])
        print()
    # removing items in list
    elif choi == 2:
        count = 0
        item_count = 0
        removed_name = input("Enter name to remove: ")
        # searching for named input to remove its item
        for i in inventory:
            item_count += 1
            # condition if the name in list is equal to name input
            if removed_name == i[0]:
                inventory.remove(i)
                print(
                    f"the {removed_name} is successfully removed in item {item_count}!"
                )
                count += 1
        # if name is not found this will print
        if count == 0:
            print(f"the {removed_name} does not exist!")
        print()
    # updating item quantity
    elif choi == 3:
        update = 0
        update_name = input("Enter name to update its quantity: ")
        for i in inventory:
            if update_name == i[0]:
                i[1] = int(input("Enter quantity to update: "))
                print("Successfully update!")
                update += 1
        # display when not found
        if update == 0:
            print(f"{update_name} does not exist!")
        print()
    # displaying items in inventory
    elif choi == 4:
        print("Items in inventory:")
        # printing all items in inventory
        for i in range(len(inventory)):
            print(
                f"item{i+1}: name: {inventory[i][0]} | quantity: {inventory[i][1]} | price: {inventory[i][2]}"
            )
        print()
    # searching name in list of items
    elif choi == 5:
        search = 0
        search_name = input("Enter Name: ")
        count_inventory = 0
        # if name was found in items it will print its name,quantity and price
        for i in inventory:
            count_inventory += 1
            if search_name == i[0]:
                print(f"{search_name} is found in item {count_inventory}")
                print(f"name: {i[0]} | quantity: {i[1]} | price: {i[2]}")
                search += 1
        # display when not found
        if search == 0:
            print(f"{search_name} is not found.")
        print()
    # exit if user input 6
    elif choi == 6:
        print("Exit")
        break
    # it will display if the input is invalid
    else:
        print("Invalid input")
        print()
