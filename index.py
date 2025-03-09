import tkinter as tk
from tkinter import ttk
from tkinter import * 
from crud import *



f = tk.Tk()
f.title("Gestion de stock avec tkinter")
f.geometry("800x500")
f.resizable(height=False, width=False)
f['bg']='antiquewhite'

def raffraichir():
    categories = lister_categorie()
    for item in tab.get_children():
        tab.delete(item)
        
    for cat in categories:
        tab.insert("","end",values=(cat[0], cat[1]))
    
def formulaire_ajout():
    f_ajout = Toplevel()
    f_ajout.title("Ajout d'une catégorie")
    f_ajout.geometry("300x200")
    f_ajout['bg']='steel blue'
    
    label_nom = Label(f_ajout, text="Nom de la catégorie")
    label_nom.pack(pady=10)
    e_nom = Entry(f_ajout)
    e_nom.pack(pady=10)
    
    b_valider = Button(f_ajout, text="Valider", fg='white', bg='green',command = lambda: enregistrer(e_nom,f_ajout))
    b_valider.pack(pady=10)
    
def enregistrer(e_nom,f_ajout):
    nom = e_nom.get()
    inserer_categorie(nom)
    raffraichir()
    f_ajout.destroy()
    


btn_ajout = Button(f, text="Ajouter une catégorie", fg="white", bg="green", command=formulaire_ajout)
btn_ajout.pack(side="top", padx=10, pady=10)
frame = tk.Frame(f)
frame.pack(pady=150,padx=50)

titre = Label(frame,text="Gestion des catégories",font=('Verdana',10,'italic bold'), fg='white', bg='black')
titre.pack()
tab = ttk.Treeview(frame,columns=("Id","Nom"),show="headings")
tab.heading("Id",text="ID")
tab.heading("Nom",text="NOM")


categories = lister_categorie()
for cat in categories:
    tab.insert("","end",values=(cat[0], cat[1]))
tab.pack()


f.mainloop()
