import csv
from config import FILENAME


def add_person():
    name = input("name: ")
    age = input("age: ")
    city = input("city: ")

    with open(FILENAME, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([name, age, city])

    print("person added!")


def show_people():
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file, fieldnames=["name", "age", "city"])
            count = 1
            for row in reader:
                print(f"{count}- {row['name']} {row['age']} year lives in {row['city']}")
                count += 1
    except FileNotFoundError:
        print("file not exist yet!")


def search_person():
    search_name = input("search name: ").lower()
    found = False

    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file, fieldnames=["name", "age", "city"])

            for row in reader:
                if row["name"].lower() == search_name:
                    print(f"Found: {row['name']} {row['age']} year lives in {row['city']}")
                    found = True
                    break

        if not found:
            print("person not found!")

    except FileNotFoundError:
        print("file not exist yet!")


def delete_person():
    delete_name = input("delete name: ").lower()
    people = []
    found = False

    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file, fieldnames=["name", "age", "city"])

            for row in reader:
                if row["name"].lower() != delete_name:
                    people.append([row["name"], row["age"], row["city"]])
                else:
                    found = True

        with open(FILENAME, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(people)

        if found:
            print("person deleted!")
        else:
            print("person not found!")

    except FileNotFoundError:
        print("file not exist yet!")


def update_person():
    update_name = input("who to update: ").lower()
    people = []
    found = False

    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file, fieldnames=["name", "age", "city"])

            for row in reader:
                if row["name"].lower() == update_name:
                    new_age = input("new age: ")
                    new_city = input("new city: ")

                    people.append([row["name"], new_age, new_city])
                    found = True
                else:
                    people.append([row["name"], row["age"], row["city"]])

        with open(FILENAME, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(people)

        if found:
            print("person updated!")
        else:
            print("person not found!")

    except FileNotFoundError:
        print("file not exist yet!")