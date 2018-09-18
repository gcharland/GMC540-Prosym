class Compagnie(object):
    argent = 0
    employes = 0
    matiere = 0
    mois = 1

    def __init__(self, argent, employes, matiere, mois):
        self.argent = argent
        self.employes = employes
        self.matiere = matiere
        self.mois = mois

    def achat(self, fournisseur, volume):
        while volume > fournisseur.vol_max:
            print("Volume demandé trop grand, veuillez commander maximum " + str(fournisseur.vol_max))
            volume = int(input("Quel volume souhaitez-vous commander?: "))

        print("Achat de " + str(volume) + "PPM au " + str(self.mois) + "em mois")

        prix_unitaire = fournisseur.get_price(volume, self.mois)
        print("Prix unitaire de " + str(prix_unitaire) + "$")
        print("Fraix fixes de " + str(fournisseur.initial_cost) + "$")
        print("Dépense de " + str(prix_unitaire*volume + fournisseur.initial_cost) + "$")
        self.argent -= prix_unitaire*volume + fournisseur.initial_cost
        self.matiere += volume
