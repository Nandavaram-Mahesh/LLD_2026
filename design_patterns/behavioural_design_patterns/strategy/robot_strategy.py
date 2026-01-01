from abc import ABC , abstractmethod

# AbstractStrategies
class Talkable(ABC):
    @abstractmethod
    def talk(self):
        pass

class Walkable(ABC):
    @abstractmethod
    def walk(self):
        pass

class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass
    
class Projectable(ABC):
    @abstractmethod
    def project(self):
        pass

# Concrete Strategies

class NormalTalk(Talkable):
    
    def talk(self):
        print('This is a NormlTalking Robot')

class NoTalk(Talkable):
    
    def talk(self):
        print('This is a NonTalking Robot')

class NormalWalk(Walkable):
    
    def walk(self):
        print('This is a NormalWalking Robot')
    
class NoWalk(Walkable):
    
    def walk(self):
        print('This is a NonWalking Robot')

class NormalFly(Flyable):
    
    def fly(self):
        print('This is a NormalFlying Robot')

class NoFly(Flyable):
    
    def fly(self):
        print('This is a NonFlying Robot')
 
class CompanionRobot(Projectable):
    
    def project(self):
        print("This is a Companion Robot")

class WalkableRobot(Projectable):
    
    def project(self):
        print("This is a walkable Robot")
        




class Robot:
    
    def __init__(self,talkable:Talkable ,walkable:Walkable,flyable:Flyable,projectable:Projectable):
        self.talkable = talkable
        self.walkable = walkable
        self.flyable = flyable
        self.projectable = projectable
    
    def walk(self):
        self.walkable.walk()
    
    def talk(self):
        self.talkable.talk()
    
    def fly(self):
        self.flyable.fly()
    
    def project(self):
        self.projectable.project()






# Client Code

robot = Robot(
NormalTalk(),
NormalWalk(),
NormalFly(),
CompanionRobot()
)

robot.walk()
robot.talk()
robot.fly()
robot.project()    
