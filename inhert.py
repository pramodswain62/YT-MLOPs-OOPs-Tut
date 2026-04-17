#base class
class Animal:
    def __init__(self):
        self.name = "buddy"

    def speak(self):
        print(self.name, "makes a sound")

#derived class
class Dog(Animal):
    def __init__(self, breed):
        super().__init__()
        self.breed = breed
        # self.behavior = 'ffriendly'
    def speak(self):
        super().speak()
        print(self.name,"bark he is ", self.breed)


animal = Animal()
animal.speak()
dog = Dog("Golden r")
dog.speak()