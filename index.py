import tkinter as tk
from tkinter import ttk
from tkinter import * 
from crud import *
from tkinter import messagebox



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
    
def confirmer_sup():
    ligne_s = tab.selection()
    if not ligne_s:
        messagebox.showwarning("Veuillez sélectionner la catégorie avant de cliquer sur supprimer")
        return
    confirm=messagebox.askyesno("Confirmation", "Etes vous sûr de vouloir supprimer cette catégorie")
    
    if confirm:
        ligne_id = tab.item(ligne_s,"values")[0]
        supprimer_categorie(ligne_id)
        raffraichir()
        messagebox.showinfo("Succès", "La catégorie a été supprimée avec succès.")
    else:
        messagebox.showinfo("Annulé", "La suppression a été annulée.")

def f_modifier():
    ligne_s = tab.selection()
    if not ligne_s:
        messagebox.showwarning("Veuillez sélectionner la catégorie avant de cliquer sur modifimer")
        return
    
    ligne_id = tab.item(ligne_s,"values")[0]
    ligne_nom = tab.item(ligne_s,"values")[1]
    
    f_modif = Toplevel()
    f_modif.title("Formulaire de modification de la catégorie")
    f_modif.geometry("300x200")
    f_modif['bg']='steel blue'
    
    l_nom = Label(f_modif,text="Nouveau nom")
    l_nom.pack(pady=10)
    
    e_nom = Entry(f_modif)
    e_nom.insert(0,ligne_nom)
    e_nom.pack(pady=10)
    
    b_valider = Button(f_modif,text="Enregistrer",fg='white',bg='green',command=lambda:enregistrer_modif(ligne_id,e_nom,f_modif))
    b_valider.pack(pady=10)
def enregistrer_modif(ligne_id,e_nom,f_modif):
    nouveau_nom = e_nom.get()
    modifier_categorie(ligne_id,nouveau_nom)
    raffraichir()
    f_modif.destroy()

b_frame = tk.Frame(f,bg='grey')
b_frame.pack(fill='x',pady=10)

b_ajouter = Button(b_frame,text="Ajouter",fg='white',bg='green',font=("Arial", 10, "bold"),pady=5,padx=15,command=formulaire_ajout)
b_ajouter.pack(side='left',padx=10)
b_supprimer = Button(b_frame,text="Supprimer",fg='white',bg='red',font=("Arial", 10, "bold"),pady=5,padx=15,command=confirmer_sup)
b_supprimer.pack(side='right',padx=10)
b_modifier = Button(b_frame,text="Modifier",fg='black',bg='#FFB84D',font=("Arial", 10, "bold"),pady=5,padx=15,command=f_modifier)
b_modifier.pack(side='right',padx=10)



frame = tk.Frame(f)
frame.pack(pady=150,padx=50)

titre = Label(frame,text="Gestion des catégories",font=('Verdana',10,'italic bold'), fg='white', bg='black')
titre.pack()
tab = ttk.Treeview(frame,columns=("Id","Nom"),show = "headings")
tab.heading("Id",text="ID")
tab.heading("Nom",text="NOM")



categories = lister_categorie()
for cat in categories:
    tab.insert("","end",values=(cat[0], cat[1]))
tab.pack()


f.mainloop()
