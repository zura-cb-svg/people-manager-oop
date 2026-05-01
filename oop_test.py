class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
        print(f"Name: {self.name} | Age: {self.age} | City: {self.city}")


class PeopleManager:
    def __init__(self):
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def show_people(self):
        print("\n--- ALL PEOPLE ---")
        for person in self.people:
            person.introduce()

    def search_person(self, name):
        print(f"\n--- SEARCH: {name} ---")
        for person in self.people:
            if person.name == name:
                print("Found:")
                person.introduce()
                return
        print("Not found")


# გამოყენება
manager = PeopleManager()

p1 = Person("zura", 17, "kutaisi")
p2 = Person("luka", 18, "tbilisi")
p3 = Person("nika", 19, "batumi")

manager.add_person(p1)
manager.add_person(p2)
manager.add_person(p3)

manager.show_people()

manager.search_person("luka")