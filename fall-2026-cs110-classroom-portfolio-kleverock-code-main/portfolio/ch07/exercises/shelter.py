import time
class Animal:
    def __init__(self):
        self.name = "abc"
        self.type = "def"
        self.id = id(x)
        self.date = time.strftime("1/1/1")

x = [1, 2, 3, 4]

a1 = Animal()
a1.name = "Suzie"
a1.type = "Dog"
a1.id = id(1)
a1.date = ("3/15/2026")
a2 = Animal()
a2.name = "Rebecca"
a2.type = "Dog"
a2.id = id(2)
a2.date = ("8/21/2026")
a3 = Animal()
a3.name = "Snowball"
a3.type = "Rabbit"
a3.id = id(3)
a3.date = ("1/10/2026")

def main():
    print(a1.name, a1.type, a1.id, a1.date)
    print(a2.name, a2.type, a2.id, a2.date)
    print(a3.name, a3.type, a3.id, a3.date)
main()