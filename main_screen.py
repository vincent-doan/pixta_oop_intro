from management_tool import *
import colorama
from colorama import Fore

colorama.init(autoreset=True)

if __name__ == "__main__":
    # create a command line ui, with numbers for functionality
    management_tool = ManagementTool()
    while True:
        print("\n1. Add room type")
        print("2. Remove room type")
        print("3. Add room")
        print("4. Remove room")
        print("5. Add guest")
        print("6. Remove guest")
        print("7. Compute cost for guest")
        print("8. Show available rooms")
        print("9. Show occupied rooms")
        print("10. Compute revenue between dates")
        print("11. Quit\n")
        choice = input("> Enter choice: ")
        
        if choice == "1":
            type_name = input("Enter room type name: ")
            price = int(input("Enter price: "))
            try:
                management_tool.add_room_type(type_name, price)
                print(Fore.LIGHTBLUE_EX + "Room type added")
            except Exception as e:
                print(Fore.RED + e.message)
        
        elif choice == "2":
            type_name = input("Enter room type name: ")
            try:
                management_tool.remove_room_type(type_name)
                print(Fore.LIGHTBLUE_EX + "Room type removed")
            except Exception as e:
                print(Fore.RED + e.message)

        elif choice == "3":
            room_name = input("Enter room name: ")
            type_name = input("Enter room type name: ")
            try:
                management_tool.add_room(room_name, type_name)
                print(Fore.LIGHTBLUE_EX + "Room added")
            except Exception as e:
                print(Fore.RED + e.message)

        elif choice == "4":
            room_name = input("Enter room name: ")
            try:
                management_tool.remove_room(room_name)
                print(Fore.LIGHTBLUE_EX + "Room removed")
            except Exception as e:
                print(Fore.RED + e.message)

        elif choice == "5":
            full_name = input("Enter full name: ")
            age = int(input("Enter age: "))
            id_card_num = input("Enter ID card number: ")
            is_vip = input("Is VIP (y/n): ") == "y"
            start_date = input("Enter start date (yyyy-mm-dd): ")
            end_date = input("Enter end date (yyyy-mm-dd): ")
            start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
            end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
            try:
                management_tool.add_guest(full_name, age, id_card_num, is_vip, start_date, end_date)
                print(Fore.LIGHTBLUE_EX + "Guest added")
            except Exception as e:
                print(Fore.RED + e.message)

        elif choice == "6":
            id_card_num = input("Enter ID card number: ")
            try:
                management_tool.remove_guest(id_card_num)
                print(Fore.LIGHTBLUE_EX + "Guest removed")
            except Exception as e:
                print(Fore.RED + e.message)

        elif choice == "7":
            id_card_num = input("Enter ID card number: ")
            try:
                print(Fore.LIGHTBLUE_EX + management_tool.compute_cost_for_guest(id_card_num))
            except Exception as e:
                print(Fore.RED + e.message)
            
        elif choice == "8":
            if len(management_tool.show_available_rooms()) == 0:
                print(Fore.RED + "No available rooms")
            else:
                print(Fore.LIGHTBLUE_EX + " ".join(management_tool.show_available_rooms()))

        elif choice == "9":
            if len(management_tool.show_occupied_rooms()) == 0:
                print(Fore.RED + "No occupied rooms")
            else:
                print(Fore.LIGHTBLUE_EX + " ".join(management_tool.show_occupied_rooms()))

        elif choice == "10":
            start_date = input("Enter start date (yyyy-mm-dd): ")
            end_date = input("Enter end date (yyyy-mm-dd): ")
            start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
            end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
            print(Fore.LIGHTBLUE_EX + str(management_tool.computer_total_revenue_between(start_date, end_date)))

        elif choice == "11":
            print(Fore.LIGHTBLUE_EX + "Goodbye")
            break