# Think of composition as a has a relationship.
# A car "has an" engine, a person "has a" name, etc.

# Think of inheritance as an is a relationship.
# A car "is a" vehicle, a person "is a" mammal, etc.

# INHERITANCE:
class Person(object):

    def __init__(self, name, hair_color):
        self.name = name
        self.hair_color = hair_color

    def greet(self):
        print("Hi, I'm %s" % self.name)

    def __str__(self):
        return self.name


class Employee(Person):

    def __init__(self, name, hair_color, position):
        super(Employee, self).__init__(name, hair_color)
        self.position = position

    def __str__(self):
        return '%s the %s' % (self.name, self.position)

marie = Person('Marie', 'blue')
john_baker = Employee('John', 'black', 'baker')

print marie
print john_baker


# COMPOSITION
class PersonWithJob():

    def __init__(self, person, position):
        self.person = person
        self.position = position

    def greet(self):
        return self.person.greet()

    def __str__(self):
        return '%s the %s' % (self.person.name, self.position)


marie_the_ceo = PersonWithJob(marie, 'CEO')
print marie_the_ceo
