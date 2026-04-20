from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

avis_lise =[]

@app.route('/')
def accueil():
    titre = "Edufeedback"
    description = "Plateforme d'analyse des retours étudiants"
    return render_template('index.html', title=titre, description=description)

@app.route('/avis', methods=['GET', 'POST'])
def avis():
    erreurs=[]

    if request.method == 'POST':    
        #recuperation des données du formulaire
        nom = request.form['nom'].strip()
        filiere = request.form['filiere'].strip()
        cours = request.form['cours'].strip()
        enseignant = request.form['enseignant'].strip()
        note = request.form['note'].strip()
        commentaire = request.form['commentaire'].strip()

        #condition de validation 
        if not nom or len(nom)<3 :
            erreurs.append("Le nom doit contenir au moins 3 caracteres")
        if not cours or len(cours)<2 :
            erreurs.append("Le cours doit contenir au moins 2 caracteres")
        if not commentaire or len(commentaire)<2 :
            erreurs.append("Le commentaire doit contenir au moins 2 caracteres")
        

        #s'il y a pas d'erreurs

        if not erreurs :
            nouvel_avis = {
                "nom" :nom,
                "filiere": filiere,
                "cours": cours,
                "enseignant": enseignant,
                "note": note,
                "commentaire": commentaire,
            }
            avis_lise.append(nouvel_avis)
            return redirect(url_for('confirmation',nom=nom, filiere=filiere, cours=cours, enseignant=enseignant, note=note, commentaire=commentaire))
        
        #s'il y a des erreurs
    return render_template('avis.html', erreurs=erreurs)
    
@app.route('/confirmation', methods=['GET', 'POST'])
def confirmation():
    nom   = request.args.get('nom')
    cours = request.args.get('cours')
    note  = request.args.get('note')
    return render_template('confirmation.html', nom=nom, cours=cours, note=note)
    
if __name__ == '__main__':
    app.run(debug=True)