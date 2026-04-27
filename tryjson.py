import json

filename = "try.json"

def add_person():
    name = input("name:")
    age = input("age:")
    city = input("city:")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            people = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        people = []

    new_person = {
        "name": name,
        "age": age,
        "city": city
    }

    people.append(new_person)

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(people, file, indent=4)
    print("person added")

def show_people():
    try:
        with open(filename, "r", encoding="utf-8") as file:
            people = json.load(file)
            count = 1
            for person in people:
                print(f"{count}- {person['name']} {person['age']}  year, lives in {person['city']}")
                count += 1
    except (FileNotFoundError, json.JSONDecodeError):
        print("file not created yet")

def search_person():
    search_name = input("search name:").lower()
    found = False
    try:
        with open(filename, "r", encoding="utf-8") as file:
            people = json.load(file)
            for person in people:
                if person['name'].lower() == search_name:
                    print(f"Found: {person['name']} {person['age']}  year, lives in {person['city']}")
                    found = True
                    break
        if not found:
            print("PERSON NOT FOUND!")
    except (FileNotFoundError, json.JSONDecodeError):
        print("file not created")

def delete_person():
    delete_name = input("who to delete:").lower()
    found = False
    new_people = []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            people = json.load(file)
            for person in people:
                if person['name'].lower() != delete_name:
                    new_people.append(person)
                else:
                    found = True
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(new_people, file, indent=4)
        if found:
            print("deleted")
        else:
            print("person not found")
    except (FileNotFoundError, json.JSONDecodeError):
        print("file not created")
    
