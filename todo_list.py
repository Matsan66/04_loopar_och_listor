def show_menu():

    """
        A user menu

        Function prints the program menu.

        """
    print("\nTodo list meny")
    print("-----------------")
    print("1. Visa menyn")
    print("2. Se innehållet i din lista")
    print("3. Lägg till nya uppgifter i din lista")
    print("4. Markera uppgift som klar")
    print("5. Hantera klara uppgifter")
    print("6. Avsluta programmet\n")



def user_menu_selection():

    """
        User menu selection

        Function asks the user to select an option from the menu.

        Returns:
            int: user menu selection 1 - 5
    """

    while True:
        user_value_selected = input("\nVad vill du göra (1 - 6): ")

        try:
            user_value_selected = int(user_value_selected)
        except ValueError:
            print("\nDu måste välja ett tal mellan 1 - 5.")
            continue

        if user_value_selected in range(1, 7):
            return user_value_selected

        print("\nDu måste välja ett tal mellan 1 - 6.")



def view_todo_list(todo_list):

    """
        View todo_list

        Function prints the list

    """
    print("\nDin todo list:")
    print("----------------")

    for i in range(len(todo_list)):
        print(f"{i + 1}. {todo_list[i]}")



def add_item_to_list(todo_list):

    """
        Add task to the list

        Function adds tasks to the list

    """

    while True:
        item_to_add = input("\nVad vill du lägga till i listan: ")
        item_to_add = item_to_add.strip()

        if item_to_add:
            todo_list.append(item_to_add)
            print(f"Ok, lade till {item_to_add} i listan")
            return

        print("\nDu måste skriva en uppgift att lägga till i listan.")



def set_finished_task(todo_list, finished_items_list, ):

    """
        Moves task from the list

        Function moves tasks from the list to finished items list

    """

    if not todo_list:
        print("\nDet finns inga uppgifter att ta bort i listan.")
        return

    view_todo_list(todo_list)

    while True:

        item_to_remove = input("\nVilken uppgift är du färdig med: ")

        try:
            item_to_remove = int(item_to_remove)
        except ValueError:
            print("Du måste välja en uppgift med dess nummer: ")
            continue

        if item_to_remove in range(1, len(todo_list) + 1):
            item_removed = todo_list.pop(item_to_remove - 1)
            finished_items_list.append(item_removed)
            print(f"Ok, {item_removed} är klar och borttagen från listan.")

            return

        view_todo_list(todo_list)
        print("\nDu måste välja en uppgift med dess nummer!")



def handle_finished_task(todo_list, finished_items_list):

    """
            Moves task from finished items list

            Function moves tasks from finished items list back to the list

    """

    if not finished_items_list:
        print("\nDet finns inga borttagna uppgifter att hantera.")
        return

    while True:

        print("\nDin lista med färdiga uppgifter:")
        print("----------------------------")

        for i in range(len(finished_items_list)):
            print(f"{i + 1}. {finished_items_list[i]}")

        restore_item_chooice = input("\nVill du lägga tillbaka en uppgift till todo listan (ja/ nej): ")

        if restore_item_chooice.lower() == "nej":
            return

        if restore_item_chooice.lower() != "ja":
            print("Du måste svara ja eller nej")
            continue

        restore_item_selection = input("Vilken uppgift vill du återställa?")

        try:
            restore_item_selection = int(restore_item_selection)
        except ValueError:
                print("Du måste välja en uppgift med dess nummer: ")
                continue

        if restore_item_selection in range(1, len(finished_items_list) + 1):
            item_restored = finished_items_list.pop(restore_item_selection - 1)
            todo_list.append(item_restored)
            print(f"Ok, {item_restored} är flyttat till todo listan.")

        else:
            print("Ogiltigt val")



def main():

    """
        Runs the program

        Controls the program execution based on user manu selections

    """

    show_menu()

    todo_list = ["Köpa mjölk", "Mata katten", "Besikta bilen"]
    finished_items_list = []

    while True:
        user_selected_menu_option = user_menu_selection()


        if user_selected_menu_option == 6:
            print("\nVälkommen åter!")
            break

        match user_selected_menu_option:
            case 1:
                show_menu()
            case 2:
                view_todo_list(todo_list)
            case 3:
                add_item_to_list(todo_list)
            case 4:
                set_finished_task(todo_list, finished_items_list)
            case 5:
                handle_finished_task(todo_list, finished_items_list)


if __name__ == "__main__":
    main()