import csv
import time

filename = "practice.csv"


def file_exists():
    try:
        with open(filename, "r", encoding="utf-8"):
            return True
    except FileNotFoundError:
        return False


def add_person():
    name = input("Enter name: ").strip()
    age = input("Enter age: ").strip()
    city = input("Enter city: ").strip()

    # validation
    if not name or not age or not city:
        print("All fields are required!")
        return

    # duplicate check
    people = []
    if file_exists():
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for person in reader:
                if person["name"].lower() == name.lower():
                    print("Person already exists!")
                    return
                people.append(person)

    # write (append)
    file_empty = not file_exists() or open(filename).read().strip() == ""

    with open(filename, "a", newline="", encoding="utf-8") as file:
        fieldnames = ["name", "age", "city"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # header only ერთხელ
        if file_empty:
            writer.writeheader()

        writer.writerow({
            "name": name,
            "age": age,
            "city": city
        })

    print("Person added!")


def show_people():
    try:
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            count = 1
            for person in reader:
                print(f"{count}- {person['name']} {person['age']} year old lives in {person['city']}")
                count += 1

    except FileNotFoundError:
        print("File not created yet!")


def search_person():
    search_name = input("Search name: ").lower()
    found = False

    try:
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for person in reader:
                if person["name"].lower() == search_name:
                    print(f"Found: {person['name']} {person['age']} year old lives in {person['city']}")
                    found = True
                    break

        if not found:
            print("Person not found!")

    except FileNotFoundError:
        print("File not created yet!")


def delete_person():
    delete_name = input("Delete name: ").lower()
    found = False
    people = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for person in reader:
                if person["name"].lower() != delete_name:
                    people.append(person)
                else:
                    found = True

        with open(filename, "w", newline="", encoding="utf-8") as file:
            fieldnames = ["name", "age", "city"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(people)

        if found:
            print("Person deleted!")
        else:
            print("Person not found!")

    except FileNotFoundError:
        print("File not created yet!")


def update_person():
    update_name = input("Who to update: ").lower()
    found = False
    people = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for person in reader:
                if person["name"].lower() == update_name:
                    new_age = input("New age: ").strip()
                    new_city = input("New city: ").strip()

                    people.append({
                        "name": person["name"],
                        "age": new_age,
                        "city": new_city
                    })
                    found = True
                else:
                    people.append(person)

        with open(filename, "w", newline="", encoding="utf-8") as file:
            fieldnames = ["name", "age", "city"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(people)

        if found:
            print("Person updated!")
        else:
            print("Person not found!")

    except FileNotFoundError:
        print("File not created yet!")


def main():
    while True:
        print("\n--- MENU ---")
        print("1 - Add person")
        print("2 - Show people")
        print("3 - Search person")
        print("4 - Delete person")
        print("5 - Update person")
        print("6 - Exit")
        print("---------------")

        choice = input("Enter the action: ")
        time.sleep(0.3)

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

        else:
            print("Invalid choice!")


main() 