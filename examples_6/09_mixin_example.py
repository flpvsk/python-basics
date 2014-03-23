class Pet(object):
    def __str__(self):
        return '%s the Pet' % self.type


class HasSound(object):
    def do_sound(self):
        print "%s says: %s" % (self, self.sound)


class Dog(Pet, HasSound):
    type = 'Dog'
    sound = 'bark'


class Cat(Pet, HasSound):
    type = 'Cat'
    sound = 'meow'


class Fox(Pet):
    type = 'fox'


dog = Dog()
cat = Cat()
fox = Fox()

dog.do_sound()
cat.do_sound()
try:
    fox.do_sound()
except AttributeError:
    print("What does the Fox say!?")
