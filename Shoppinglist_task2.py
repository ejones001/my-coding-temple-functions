def add_to_list(shopping_list, item):
    shopping_list.append(item)
    print(f"{item} has been added to the list.")

def remove_from_list(shopping_list, item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} has been removed from the list.")
    else:
        print(f"{item} is not in the list.")
