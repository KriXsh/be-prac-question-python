

class Animal():
    def speak(self):
        raise NotImplementedError("Subclass must implement this method")

class Dog(Animal):
    def speak(self):
        print("woof")

dog = Dog()
dog.speak()