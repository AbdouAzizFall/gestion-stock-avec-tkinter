import sqlite3
from connexion import crer_une_connexion

def inserer_categorie(nom_cat):
    try:
        conn = crer_une_connexion()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO categorie (nom_cat) VALUES (?)",(nom_cat,))
        conn.commit()
        print("Catégorie ", nom_cat," ajoutée avec succés!")
    except sqlite3.Error as e:
        print(f"Erreur lors de l'insertion : {e}")
    
    finally:
        if conn:
            cursor.close()
            conn.close()
#inserer_categorie("Chaussure")
#inserer_categorie("Montre")
def inserer_produit(lib_p, qte_p, pu_p, id_categorie):
    try:
        conn = crer_une_connexion()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO produit (lib_p, qte_p, pu_p, id_categorie) VALUES (?,?,?,?)",(lib_p, qte_p, pu_p, id_categorie,))
        conn.commit()
        print("Produit ", lib_p," ajoutée avec succés!")
    except sqlite3.Error as e:
        print(f"Erreur lors de l'insertion : {e}")
    
    finally:
        if conn:
            cursor.close()
            conn.close()
#inserer_produit("Timberland",25,12000,1)
#inserer_produit("New balance",25,12000,1)
#inserer_produit("Rolex",12,25000,2)
