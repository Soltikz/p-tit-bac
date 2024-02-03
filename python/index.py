from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ajouter_jour', methods=['POST'])
def ajouter_jour():
    pseudonyme = request.form.get('pseudonyme')

    if pseudonyme:
        # Redirection vers la page "lobby" avec le pseudonyme en tant que paramètre
        return redirect(url_for('lobby', pseudonyme=pseudonyme))
    else:
        return 'Veuillez saisir un pseudonyme valide.'

@app.route('/lobby/<pseudonyme>')
def lobby(pseudonyme):
    return f'Bienvenue dans le lobby, {pseudonyme} !'

if __name__ == '__main__':
    app.run(debug=True)
