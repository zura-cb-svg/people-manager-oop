import csv
import time

filename="day3.csv"

def add_person():
    name=input("name:")
    age=input("age:")
    city=input("city:")
 
    with open(filename, "a", newline="", encoding="utf-8") as file:
        writer=csv.writer(file)
        writer.writerow([name, age, city])

    print("person added!")

def show_people():
   try: 
    with open(filename, "r", encoding="utf-8") as file:
        reader=csv.DictReader(file, fieldnames=["name", "age", "city"])
        count=1
        for row in reader:
           
            print(f"{count}- {row['name']} {row['age']} year lives in {row['city']}")
            count+=1
   except FileNotFoundError:
      print("file not exist yet!")
def search_person():
 try:
    search_name=input("search name:").lower()
    found=False

    with open(filename, "r", encoding="utf-8") as file:
        reader=csv.DictReader(file, fieldnames=["name", "age", "city"])
        for row in reader:
            if row["name"].lower()==search_name:

             print(f" Found: {row['name']} {row['age']} year lives in {row['city']}")
             found=True
             break
        if not found:
            print("person not found!")
 except FileNotFoundError:
    print("file not created yet")

def delete_person():
 try:
    delete_name=input("delete name:").lower()
    people=[]
    found=False

    with open(filename, "r", encoding="utf-8") as file:
        reader=csv.DictReader(file, fieldnames=["name", "age", "city"])
        for row in reader:
            if row["name"]!=delete_name:
                people.append([row["name"], row["age"], row["city"]])
            else:
                found=True
        with open(filename, "w", newline="", encoding="utf-8") as file:
           writer=csv.writer(file)
           writer.writerows(people)
        if  found:
                print("person deleted!")
        else:
             print("person not found!")
 except FileNotFoundError:
    print("file not exist yet!")

def update_person():
    try:
        update_name = input("who to update: ").lower()
        people = []
        found = False

        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file, fieldnames=["name", "age", "city"])

            for row in reader:
                if row["name"].lower() == update_name:
                    new_age = input("new age: ")
                    new_city = input("new city: ")

                    people.append([row["name"], new_age, new_city])
                    found = True
                else:
                    people.append([row["name"], row["age"], row["city"]])

        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(people)

        if found:
            print("updated!")
        else:
            print("person not found!")

    except FileNotFoundError:
        print("file not exist")

def main():
    while True:
     print("\n---menu---")
     print("1-add person")
     print("2-show people")
     print("3-search person")
     print("4-delete person")
     print("5-update person")
     print("6-exit")
     print("---------------)")
     choice=input("enter the action:")
     time.sleep(0.5)

     if choice=="1":
       add_person()

     elif choice=="2":
      show_people()
  
     elif choice=="3":
       search_person()

     elif choice=="4":
      delete_person()
    
     elif choice=="5":
      update_person()

     elif choice=="6":
      print("goodbye sir!")
      break
main()
     