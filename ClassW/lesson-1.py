class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def grow(self):
        self.age += 1
        print(self.name, "став стрше", self.age)

cat1 = Cat("Киса", 7)
cat2 = Cat("Барсик", 8)

print(cat1.name)
print(cat1.age)

print(cat2.name)
print(cat2.age)

cat1.grow()