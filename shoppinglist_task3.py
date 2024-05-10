def add_to_list(shopping_list, item):
    shopping_list.append(item)
    print(f"{item} has been added to the list.")

def remove_from_list(shopping_list, item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} has been removed from the list.")
    else:
        print(f"{item} is not in the list.")

def print_list(shopping_list):
    if shopping_list:
        print("Your Shopping List:")
        for index, item in enumerate(shopping_list, start=1):
            print(f"{index}. {item}")
    else:
        print("Your shopping list is empty.")

shopping_list = []

# Add items to the list
add_to_list(shopping_list, "Apples")
add_to_list(shopping_list, "Milk")
add_to_list(shopping_list, "Bread")

# Remove items from the list
remove_from_list(shopping_list, "Milk")

# Print the entire list
print_list(shopping_list)
