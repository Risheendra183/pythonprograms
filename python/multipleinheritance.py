class human:
    def eat(self):
        print("I can eat")
class Male:
    def flirt(self):
        print("i can work")
class male:
    def flirt(self):
        print("i can flirt")
    def work(self):
        print("i can code")
class Boy(human,male):
    pass

boy1=Boy()
boy1.work()