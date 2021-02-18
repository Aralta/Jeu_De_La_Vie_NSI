from grille import Grille
import tkinter as tk
import time



root = tk.Tk()
root.geometry("650x705")
app = Grille(master=root)


while True:
    app.action_generate()
    app.update_idletasks()
    app.update()
    time.sleep(1)
