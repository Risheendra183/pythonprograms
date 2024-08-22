class grandfather():
    def outputg(self):
        print("i am a grand parent")


class parent(grandfather):
    def output(self):
        print("i am a parent")
class child(parent):
    def outputc(self):
        print("i am a child")
c=child()
c.outputc()
c.output()
c.outputg()