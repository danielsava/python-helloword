class Pessoa:

    def __init__(self, name, last_name, age, curse):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.curse = curse


p1 = Pessoa('Daniel', 'Sava', 40, 'Machine Learning')

print(p1.name)
print(p1.last_name)

p1.last_name = 'Pupak'
print(p1.last_name)


p2 = Pessoa(p1.name, p1.last_name, p1.age, p1.curse)
p2.name = "Silva"


p2.

print(p2.name)

