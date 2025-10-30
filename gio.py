class Human:
    def __init__(self, name, lastname, age, weight, tall):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.weight = weight
        self.tall = tall

    def info(self):
        return f"Name: {self.name}, Lastname: {self.lastname}, Age: {self.age}, Weight: {self.weight}, Tall: {self.tall}"

x = Human("Gio", "Gorjoladze", 22, 80)
print(x.info())