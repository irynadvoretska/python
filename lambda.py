people = [
    {"name": "Harry", "house": "Griffindor"},
    {"name": "Cho", "house": "Ravenklaw"},
    {"name": "Draco", "house": "Slytherin"}
    ]

def f(person):
    return person["name"]

people.sort(key=f)

print(people)