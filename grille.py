from cellule import Cellule
from random import Random
import tkinter as tk


class Grille(tk.Frame):
    
    def __init__(self, master=None):
        #tk init var 
        super().__init__(master)
        self.master = master
        self.pack()
        

        random = Random()
        self.width = 15
        self.height = 15
        self.grid = [[0 for i in range(self.width)] for x in range(self.height)]

        for x in range(self.width):
            for y in range(self.height):
                rand = bool(random.getrandbits(1))
                self.grid[x][y] = Cellule(self,rand, x, y)
        self.create_widgets()
        #self.render_grid()

    #create Frame method
    def create_widgets(self):
        
        self.header = tk.Frame(self.master, bg='grey', height=30)
        self.content = tk.Frame(self.master)
        self.commands = tk.Frame(self.master, bg='grey', height=30)
        self.footer = tk.Frame(self.master, bg='grey', height=30)

        self.header.pack(fill='both')  # , side='top')
        self.content.pack(fill='both')
        self.commands.pack(fill='both')
        self.footer.pack(fill='both', side='bottom')

        tittle = tk.Label(self.header)
        tittle["text"] = "Jeu de Conway"
        tittle.pack(side=tk.TOP)

        self.gridframe = tk.Frame(self.content, width=100, height=100)
        self.gridframe.pack(side=tk.TOP)
        
        self.generate_gridframe()
        
        generate = tk.Button(self.footer, text="generate", fg="grey",
                             command=self.action_generate).grid(row=0, column=0)


        purge = tk.Button(self.footer, text="purge", fg="grey",command=self.purge_grid).grid(row=0, column=1)
        quit = tk.Button(self.footer, text="QUIT", fg="grey",command=self.master.destroy).grid(row=0, column=2)
        
    
        
    def generate_gridframe(self):
        
        self.purge_grid()

        for x in range(self.width):
        
            for y in range(self.height):
                celstate = self.grid[x][y].__str__()
                frame = tk.Frame(self.gridframe, background=celstate, width=40, height=40, borderwidth=1).grid(row=x, column=y, padx=1, pady=1)
    
    #Purge the grid frame
    def purge_grid(self) : 

        for widget in self.gridframe.winfo_children():
            widget.destroy()
        self.gridframe.grid_remove()

    def action_generate(self):

        for x in range(self.width):
            for y in range(self.height):
                self.grid[x][y].get_voisins()
        
        for x in range(self.width):
            for y in range(self.height):
                self.grid[x][y].basculer()

        self.generate_gridframe()

    def get_grid_info(self,x,y):
        return self.grid[x][y].is_alive()
        
       
