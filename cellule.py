class Cellule:
    def __init__(self,grid,state,posx,posy):
        self.grid = grid
        self.posx = posx
        self.posy = posy
        self.actuel = state
        self.futur = False
        self.alive_nearby = 0


    #Retourne l'état actuel de la cellule
    def is_alive(self):
        return self.actuel

    # recupere info voisins et applique l'etat futur
    def get_voisins(self):
        cpt = 0   
        for x in range(-1, 2):
            for y in range(-1, 2):
                nearbyx = self.posx + x
                nearbyy = self.posy + y
                if x == 0 and y == 0 : 
                    cpt += 1
                else : 
                    if nearbyx > 0 and nearbyy > 0 and nearbyx < self.grid.width and nearbyy < self.grid.height:
                        if self.grid.get_grid_info(nearbyx, nearbyy):
                            self.alive_nearby += 1

        if self.actuel == False:
            if self.alive_nearby == 3:
                self.naitre()
            else:
                self.mourrir()

        elif self.actuel == True:
            if self.alive_nearby == 2 or self.alive_nearby == 3:
                self.naitre()
            else:
                self.mourrir()


    def naitre(self):
        self.futur = True
    
    def mourrir(self):
        self.futur = False

    def basculer(self):
        self.actuel = self.futur
        self.futur=False
        self.alive_nearby = 0

    def __str__(self):
        if self.actuel==True:
            return "#000000"
        elif self.actuel==False:
            return "#FFFFFF"

    
