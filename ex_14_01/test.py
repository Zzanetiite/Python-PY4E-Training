# x = 'Hello there'
# print(type(x))
# print(dir(x))

class PartyAnimal:
    x = 0
    name = ""

    def __init__(self, z):
        self.name = z
        print(self.name, "constructed")

    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)
# print(type(PartyAnimal))
# print(dir(PartyAnimal))

class FootballFan(PartyAnimal):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, "points", self.points)

# an = PartyAnimal()
# print(type(an))
# print(dir(PartyAnimal))
#
# an.party()
# an.party()
# an.party()

#Sally is the z parameter. Self is the object itself.
s = PartyAnimal("Sally")
s.party()

j = FootballFan("Jim")
j.party()
j.touchdown()
s.party()
