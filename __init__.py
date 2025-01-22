from flask import Flask, render_template

# Initialiser l'application Flask
app = Flask(__name__)

# Définir la route pour la page /welcome
@app.route('/index')
def index():
    return render_template('index.html')  # Rend le fichier HTML dans le dossier templates

@app.route('/formulaire_livre.html')
def Readfiche(post_id):
    conn = sqlite2.connect('bibliotheque.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livres)
    data = cursor.fetchall()
    conn.close()
    # Rendre le template HTML et transmettre les données
    return render_template('data.html', data=data)

# Définir la route pour afficher le formulaire d'enregistrement/suppression des livres
@app.route('/formulaire_livre.html', methods=['GET'])
def formulaire_livre():
    return render_template('formulaire_livre.html')  # afficher le formulaire

# Définir la route pour enregistrer un livre
@app.route('/formulaire_livre.html', methods=['POST'])
def enregistrer_livre():
    titre = request.form['titre']
    auteur = request.form['auteur']

    # Connexion à la base de données
    conn = sqlite2.connect('bibliotheque.db')
    cursor = connection.cursor()

    # Exécution de la requête SQL pour insérer un nouveau client
    cursor.execute('INSERT INTO livres (titre, auteur) VALUES (?, ?)', (titre, auteur))
    conn.commit()
    conn.close()
    return redirect('/Enregistrer/Supprimer un livre/')  # Rediriger vers la page d'accueil après l'enregistrement


# Démarrer l'application Flask
if __name__ == "__main__":
    app.run(debug=True)
