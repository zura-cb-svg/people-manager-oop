import json
class Person:
    def __init__(self, name, age, city):
        self.name=name
        self.age=age
        self.city=city
    
    def introduce(self):
        print(f"Name: {self.name} | Age: {self.age} | City: {self.city}")
    
    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "city": self.city
        }

class PeopleManager:
    def __init__(self):
        self.people=[]
    
    def add_person(self, person):
            self.people.append(person)
    
    def show_people(self):
        print("\n---ALL USERS---")
        if not self.people:
            print("no users yet")
            return
        for person in self.people:
            person.introduce()

    
    def search_person(self, name):
        print(f"search {name}")
        for person in self.people:
            if person.name==name:
                person.introduce()
                return
        print("user not found")
    
    def delete_person(self, name):
        print(f"delete name {name}")
        for person in self.people:
            if person.name==name:
                self.people.remove(person)
                return
        print("user not found")
    
    def count_by_city(self, city):
        count=0
        for person in self.people:
            if person.city==city:
                count+=1
        if count>0:
             print(f"city count is {count}")
             return
        print("city not found")
    
    def save_to_file(self):
        data=[]
        for person in self.people:
            data.append(person.to_dict())
        with open("people.json", "w") as file:
             json.dump(data, file)
    
    def load_from_file(self):
        try:
            with open("people.json", "r") as file:
                data=json.load(file)
                for item in data:
                    p = Person(item["name"], item["age"], item["city"]) 
                    self.people.append(p)

        except:
            print("no file yet")

manager=PeopleManager()

manager.load_from_file()
def main():
 while True:
        print("\n---MENU---")
        print(" 1 - Add person")
        print(" 2 - Show people")
        print(" 3 - Search")
        print(" 4 - Delete")
        print(" 5 - Count")
        print(" 6 - Exit") 
        print("- - - - - - - ") 

        choice = input("choose the action:")

        if choice == "1":
            name = input("name:")
            age = input("age:")
            city = input("city:")

            p = Person(name, age, city)
            manager.add_person(p)

            manager.save_to_file()  

        elif choice == "2":
            manager.show_people()

        elif choice == "3":
            search_name = input("which name do u want to find:")
            manager.search_person(search_name)

        elif choice == "4":
            delete_name = input("who to delete:")
            manager.delete_person(delete_name)

            manager.save_to_file()  

        elif choice == "5":
            city = input("city:")
            manager.count_by_city(city)

        elif choice == "6":
            print("Goodbye!")
            break


main()