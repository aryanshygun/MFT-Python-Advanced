class Person:
    region = 'London'
    def __init__(self, name):
        self.name = name

p1 = Person('Jack')
p2 = Person('John')
print(id(p1.region))
p1.region = 'Berlin'
print(p1.region)
print(id(p1.region))
