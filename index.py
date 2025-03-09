import tkinter as tk
from tkinter import ttk
from tkinter import * 
from crud import *


f = tk.Tk()
f.title("Gestion de stock avec tkinter")
f.geometry("800x500")
f.resizable(height=False, width=False)
f['bg']='antiquewhite'
btn_ajout = Button(f, text="Ajouter une catégorie", fg="white", bg="green")
btn_ajout.pack(side="top", padx=10, pady=10)
frame = tk.Frame(f)
frame.pack(pady=150,padx=50)

titre = Label(frame,text="Gestion des catégories",font=('Verdana',10,'italic bold'), fg='white', bg='black')
titre.pack()
tab = ttk.Treeview(frame,columns=("Id","Nom","Actions"),show="headings")
tab.heading("Id",text="ID")
tab.heading("Nom",text="NOM")
tab.pack()

categories = lister_categorie()
for cat in categories:
    tab.insert("","end",values=(cat[0], cat[1]))
tab.pack()
f.mainloop()
