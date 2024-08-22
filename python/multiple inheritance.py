class father():
    def outputg(self):
        print(" i am a father")


class mother():
    def output(self):
        print("i am a mother")
class child(father,mother):
    def outputc(self):
        print("i am a child")
c=child()
c.outputc()
c.output()
c.outputg()