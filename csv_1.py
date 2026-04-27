from functions import add_person, show_people, search_person, delete_person, update_person
import time

def main():
    while True:
        print("\n---menu---")
        print("1 - add person")
        print("2 - show people")
        print("3 - search person")
        print("4 - delete person")
        print("5 - update person")
        print("6 - exit")
        print("---------------")

        choice = input("Enter the action: ")
        time.sleep(0.5)

        if choice == "1":
            add_person()

        elif choice == "2":
            show_people()

        elif choice == "3":
            search_person()

        elif choice == "4":
            delete_person()

        elif choice == "5":
            update_person()

        elif choice == "6":
            print("Goodbye!")
            break

main()