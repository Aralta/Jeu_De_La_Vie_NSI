class Cellule:
    def __init__(self,grid,state,posx,posy):
        #print(super().action_generate())
        self.grid = grid
        self.posx = posx
        self.posy = posy
        self.actuel = state
        self.futur = False
        self.alive_nearby = 0
        #voisins = []

    #Retourne l'état actuel de la cellule
    def is_alive(self):
        return self.actuel

    # def set_voisins(self):

    def get_voisins(self):
        #print("get")
        for x in range(-1, 2):
            for y in range(-1, 2):
                nearbyx = self.posx + x
                nearbyy = self.posy + y
                
                if nearbyx > 0 and nearbyy > 0 and nearbyx < self.grid.width and nearbyy < self.grid.height:
                    nearby = self.grid.get_grid_info(nearbyx, nearbyy)
                    if nearby == True:
                        self.alive_nearby += 1
                
                if self.alive_nearby == 3 and self.actuel == False:
                    self.naitre()
                elif self.alive_nearby == range(2,3) and self.actuel == True:
                    self.naitre()
                else:
                    self.mourrir()

        #print("x :",self.posx ,"y :",self.posy,"alive_nei : ", self.alive_nearby)
        #return self.voisins

    def naitre(self):
        self.futur = True
    
    def mourrir(self):
        self.futur = False

    def basculer(self):
        self.actuel = self.futur
        self.futur=False

    def __str__(self):
        if self.actuel==True:
            return "#000000"
        elif self.actuel==False:
            return "#FFFFFF"

    
