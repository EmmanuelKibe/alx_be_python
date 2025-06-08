def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter the item to add: ")
            shopping_list.append(item.strip())
            
        elif choice == '2':
            # Prompt for and remove an item
            while True:
                remove_item = input("Enter the item you want to remove: ")
                
                if remove_item.strip() not in shopping_list:
                    print("Item not found! Kindly input a valid item")
                else:
                    shopping_list.remove(remove_item.strip())
                    print(f"{remove_item} has been successfuly removed")
                    break
                
        elif choice == '3':
            # Display the shopping list
            print("Shopping list:")
            for item in shopping_list:
                print(item)
                
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
# This code implements a simple shopping list manager that allows users to add, remove, and view items in their shopping list.