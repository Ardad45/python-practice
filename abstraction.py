#abstraction
#by using abstraction we can hide the implementation details and show only the functionality to the user
#abstraction can be achieved by using abstract classes and interfaces
#abstract class is a class which cannot be instantiated and it can have abstract methods and concrete methods
#by using abc module we can create abstract classes and abstract methods
from abc import*
class parent(ABC):
    @abstractmethod
    def m1(self):
        pass
t=parent() #this will give an error because we cannot create an object of abstract class
#object could not be created because the class is abstract and has abstract method m1 which is not implemented in the child class 

#concrete class is a class which can be instantiated and it can have concrete methods
#the method without decorator is called concrete method and it can be implemented in the abstract class and it can be inherited by the child class
#the method with @abstractmethod decorator is called abstract method and it must be implemented in the child class and it cannot be implemented in the abstract class
#the method which have logic is called concrete method and the method which does not have logic is called abstract method
#interface is a class which have only abstract methods and it cannot have concrete methods and it cannot be instantiated and it can be implemented by the child class
#abstract class can have both abstract methods and concrete methods but interface can have only abstract methods and it cannot have concrete methods
#concrete class can have both concrete methods and abstract methods but interface can have only abstract methods and it cannot have concrete methods

from abc import*
class tata(ABC):
    @abstractmethod
    def milage(self):
        pass
class punch(tata):
    def color(self):
        print("red")
t1=punch() #this will give an error because we cannot create an object of abstract class
#object could not be created because the class is abstract and has abstract method milage which is not implemented in the child class
from abc import*
class tata(ABC):
    @abstractmethod
    def milage(self):
        pass
class punch(tata):
    def milage(self):
        print("20km/l")
    def color(self):
        print("red")
t1=punch()
t1.milage()
t1.color()
