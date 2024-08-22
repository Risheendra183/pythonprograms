class Human:
    def __init__(self,heart):
        self.eyes=2
        self.nose=1
        self.heart=heart
    def eat(self):
        print(" i can eat")
    def work(self):
        print("i can work ")
class male(Human):
    def __init__(self,name,heart) :
        super().__init__(heart)
        self.name=name
    def flirt(self):
        print("i can flirt")
    def work(self):
        super().work()
        print("i can code")
    def display(self):
            print(f"Hi i am {self.name} and i have {self.heart} heart")
male1=male("rishi",1)
male1.flirt()
male1.work()
print(male1.eyes)
print(male1.name)
print(male1.heart)
male1.display()