import os.path


class Fichier:
    def __init__(self, file = (open("fichier.txt", "a+"))):
        self.file = file
        self.file.close()


    def ekri_fich(self):
        self.file= open("fichier.txt", "a+")
        self.file.write(input("entrer tex ou a")+"\n")
        self.file.close()

    def efase_kontni(self):
        self.file=open("fichier.txt", "w")
        pass

    def efase_fichye(self):
        if os.path.exists("fichier.txt"):
            os.remove("fichier.txt")

    def afichye_fichye(self):
        self.file = open("fichier.txt", "r+")
        print(self.file.readlines())
        self.file.close()


start = True

while start:
    print("1.afichye fichye")
    print("2.ekri nan fichye a")
    print("3.siprime kontni fichye a")
    print("4.siprime fichye a")


    a = int(input("antre chwaw la"))
    fichye = Fichier()
    if a == 1:
        fichye.afichye_fichye()

    if a ==2:
        fichye.ekri_fich()
    if a == 3:
        fichye.efase_kontni()
    if a == 4:
        fichye.efase_fichye()
        start = False





