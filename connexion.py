import sqlite3

def crer_une_connexion():
    try:
        conn = sqlite3.connect('gestion_de_stock.db')
        print("Connexion à SQLite réussie")
        return conn
    except sqlite3.Error as e:
        print(f"Connexion à SQLite échouée : {e}")
        return None


def creer_tables():
    try:
        conn = crer_une_connexion()
        cursor = conn.cursor()

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS categorie(
        id_cat INTEGER PRIMARY KEY AUTOINCREMENT,
        nom_cat TEXT NOT NULL
        )
         ''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS produit(
        id_p INTEGER PRIMARY KEY AUTOINCREMENT,
        lib_p TEXT NOT NULL,
        qte_p INTEGER NOT NULL,
        pu_p REAL NOT NULL,
        id_categorie INTEGER,
        FOREIGN KEY (id_categorie) REFERENCES categorie(id_cat) 
        )
         ''')
        conn.commit()
        print("Tables crées avec succés")

    except Error as e:
        print(f"Erreur lors de la création des tables : {e}")
    
    finally:
        if conn:
            conn.close()
creer_tables()