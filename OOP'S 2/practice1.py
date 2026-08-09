class teaher:
    def teach(self):
        print("Teaching students")

class singer:
    def sing(self):
        print("Singning song")

class person(teaher,singer):
    pass

p=person()
p.teach()
p.sing()