

class Vivan:
    def __init__(self, nom: str, laj: int, men: int, pye: int):
        self.nom = nom
        self.laj = laj
        self.men = men
        self.pye = pye

    def se_presenter(self):
        print(self.nom, "gen", self.laj, "ans", "avek", self.men, "ak", self.pye)

personne1 = Vivan("jean", 23, 4, 2)

personne2 = Vivan("lorie", 21, 4, 2)
personne2.se_presenter()
personne1.se_presenter()


class Poul(Vivan):
    def __init__(self, nom, laj, men, pye):
        super().__init__(nom, laj, men, pye)


poul = Poul("", 2, 2, 2)
poul.se_presenter()
