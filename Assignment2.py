# dog.py

class Dog:
    # Class attribute
    species = "Canis familiaris"

    # Constructor method (initializes object)
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def bark(self):
        return f"{self.name} says woof!"

    # Another instance method
    def get_info(self):
        return f"{self.name} is {self.age} years old."

# --- Object creation and method calls ---
if __name__ == "__main__":
    dog1 = Dog("Buddy", 3)
    dog2 = Dog("Lyla", 5)

    print(dog1.bark())
    print(dog2.get_info())
