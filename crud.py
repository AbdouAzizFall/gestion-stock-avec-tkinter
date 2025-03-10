import sqlite3
from connexion import creer_une_connexion

def inserer_categorie(nom_cat):
    try:
        conn = creer_une_connexion()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO categorie (nom_cat) VALUES (?)",(nom_cat,))
        conn.commit()
        print(f"Catégorie {nom_cat} ajoutée avec succés!")
    except sqlite3.Error as e:
        print(f"Erreur lors de l'insertion : {e}")
    
    finally:
        if conn:
            cursor.close()
            conn.close()
#inserer_categorie("Chaussure")
#inserer_categorie("Montre")
#inserer_categorie("Sup")
def inserer_produit(lib_p, qte_p, pu_p, id_categorie):
    try:
        conn = crer_une_connexion()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO produit (lib_p, qte_p, pu_p, id_categorie) VALUES (?,?,?,?)",(lib_p, qte_p, pu_p, id_categorie,))
        conn.commit()
        print(f"Produit {lib_p} ajoutée avec succés!")
    except sqlite3.Error as e:
        print(f"Erreur lors de l'insertion : {e}")
    
    finally:
        if conn:
            cursor.close()
            conn.close()
#inserer_produit("Timberland",25,12000,1)
#inserer_produit("New balance",25,12000,1)
#inserer_produit("Rolex",12,25000,2)
def lister_categorie():
    categories = []
    try:
        conn = creer_une_connexion()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM categorie")
        categories = cursor.fetchall()
        for cat in categories:
            print(cat)
    except sqlite3.Error as e:
        print(f"Erreur lors de l'affichage : {e}")
    
    finally:
        if conn:
            cursor.close()
            conn.close()
    return categories
#lister_categorie()
def lister_produit():
    try:
        conn = crer_une_connexion()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM produit")
        produits = cursor.fetchall()
        for cat in produits:
            print(cat)
    except sqlite3.Error as e:
        print(f"Erreur lors de l'affichage : {e}")
    
    finally:
        if conn:
            cursor.close()
            conn.close()
#lister_produit()
def modifier_categorie(id_cat,nouveau_nom):
    try:
        conn = creer_une_connexion()
        cursor = conn.cursor()
        cursor.execute("UPDATE categorie set nom_cat =? WHERE id_cat =?",(nouveau_nom,id_cat))
        conn.commit()
        print(f"Catégorie modifiée avec succés!")
    except sqlite3.Error as e:
        print(f"Erreur lors de la modification : {e}")
    
    finally:
        if conn:
            cursor.close()
            conn.close()
#modifier_categorie(2,"montre")
def modifier_produit(id_p,n_nom,n_qte,n_pu,n_categorie):
    try:
        conn = crer_une_connexion()
        cursor = conn.cursor()
        cursor.execute("UPDATE produit set lib_p=?, qte_p=?, pu_p=?, id_categorie=? WHERE id_p =?",(n_nom,n_qte,n_pu,n_categorie,id_p))
        conn.commit()
        print(f"Produit modifié avec succés!")
    except sqlite3.Error as e:
        print(f"Erreur lors de la modification : {e}")
    
    finally:
        if conn:
            cursor.close()
            conn.close()
#modifier_produit(1,"Timberland",12,25000,2)
def supprimer_categorie(id_cat):
    conn = None
    try:
        conn = creer_une_connexion()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM categorie WHERE id_cat=?",(id_cat,))
        conn.commit()
        print(f"Catégorie {id_cat}supprimée avec succés!")
    except sqlite3.Error as e:
        print(f"Erreur lors de la suppression : {e}")
    
    finally:
        if conn:
            cursor.close()
            conn.close()
    
#supprimer_categorie(3)
def supprimer_produit(id_p):
    try:
        conn = crer_une_connexion()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM produit WHERE id_p=?",(id_p,))
        conn.commit()
        print(f"Produit {id_p} supprimé avec succés!")
    except sqlite3.Error as e:
        print(f"Erreur lors de la suppression : {e}")
    
    finally:
        if conn:
            cursor.close()
            conn.close()
