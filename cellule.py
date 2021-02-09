class Cellule:
    def __init__(self,state):
        self.actuel = state
        self.futur = False
        voisins = []

    def est_vivant(self):
        return self.actuel

    # def set_voisins(self):

    def get_voisins(self):
        return self.voisins

    def naitre(self):
        self.futur = True
    
    def mourrir(self):
        self.futur = False

    def basculer(self):
        self.actuel = self.futur

    def __str__(self):
        if self.actuel==True:
            return "#000000"
        elif self.actuel==False:
            return "#FFFFFF"

    
