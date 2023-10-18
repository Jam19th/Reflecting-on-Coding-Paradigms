class Pod_Racer:
    def __init__(self, max_speed, condition, price, owner):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price
        self.owner = owner
        
    def repair(self):
        print(f"{self.owner}'s pod is being repaired!")
        self.condition = "repaired"
        
    
class Anakin_Pod(Pod_Racer):
    def __init__(self, max_speed, condition, price, owner = "Anakin Skywalker"):
        super().__init__(max_speed, condition, price, owner)
        
    def boost(self):
        print(f"{self.owner} is boosting!")
        self.max_speed *= 2
        
class Sebulba_Pod(Pod_Racer):
    def __init__(self, max_speed, condition, price, owner = "Sebulba"):
        super().__init__(max_speed, condition, price, owner)
        
    def flame_jet(self, other_pod):
        print(f"{self.owner} is using his flame jet on {other_pod.owner}'s pod!")
        other_pod.condition = "trashed"
        
anakins_pod = Anakin_Pod(25, "perfect", 1000)

sebulba_pod = Sebulba_Pod(28, "perfect", 1000000)

print(f"Anakin's pod condition: {anakins_pod.condition}")
print(f"Sebulba's pod condition: {sebulba_pod.condition}")

sebulba_pod.flame_jet(anakins_pod)

print(f"Anakin's pod condition: {anakins_pod.condition}")
print(f"Sebulba's pod condition: {sebulba_pod.condition}")

anakins_pod.repair()

print(f"Anakin's pod condition: {anakins_pod.condition}")
print(f"Sebulba's pod condition: {sebulba_pod.condition}")

print(f"Anakin's pod max speed: {anakins_pod.max_speed}")
print(f"Sebulba's pod max speed: {sebulba_pod.max_speed}")

anakins_pod.boost()

print(f"Anakin's pod max speed: {anakins_pod.max_speed}")
print(f"Sebulba's pod max speed: {sebulba_pod.max_speed}")

'''
How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
Encapsulation
Abstraction
Inheritance
Polymorphism

This solution demonstrates the four pillars of OOP in the following ways:

Encapsulation: The Pod_Racer class encapsulates the max_speed, condition, price, and owner attributes. The Anakin_Pod and Sebulba_Pod classes inherit these attributes from the Pod_Racer class. The Pod_Racer class encapsulates the repair method. The Anakin_Pod and Sebulba_Pod classes inherit this method from the Pod_Racer class. The Anakin_Pod class encapsulates the boost method. The Sebulba_Pod class encapsulates the flame_jet method.

Abstraction: The Pod_Racer class abstracts the max_speed, condition, price, and owner attributes. The Anakin_Pod and Sebulba_Pod classes inherit these attributes from the Pod_Racer class. The Pod_Racer class abstracts the repair method. The Anakin_Pod and Sebulba_Pod classes inherit this method from the Pod_Racer class. The Anakin_Pod class abstracts the boost method. The Sebulba_Pod class abstracts the flame_jet method.

Inheritance: The Anakin_Pod and Sebulba_Pod classes inherit the max_speed, condition, price, and owner attributes from the Pod_Racer class. The Anakin_Pod and Sebulba_Pod classes inherit the repair method from the Pod_Racer class.

Polymorphism: The Anakin_Pod and Sebulba_Pod classes override the __init__ method of the Pod_Racer class. The Anakin_Pod class overrides the boost method of the Pod_Racer class. The Sebulba_Pod class overrides the flame_jet method of the Pod_Racer class.
'''

'''
Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?

Yes, it would have been easier to implement a solution to this problem using a different coding style. For example, it would have been easier to implement a solution to this problem using a functional programming style.
'''

'''
How in particular did Object Oriented Programming assist in the solving of this problem?

Object Oriented Programming assisted in the solving of this problem by allowing us to write code that is easier to read and understand. It also allowed us to write code that is easier to test and debug.
'''