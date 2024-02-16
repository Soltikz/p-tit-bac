from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__, template_folder="../html")

lobby = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_player', methods=['POST'])
def add_player():
    player_name = request.form['player_name']
    lobby.append(player_name)
    return redirect(url_for('lobby', player=player_name))

@app.route('../html/lobby.html')
def lobby():
    players = ["Joueur 1", "Joueur 2", "Joueur 3"]  # Exemple de liste de joueurs
    return render_template('lobby.html', players=players)

if __name__ == '__main__':
    app.run(debug=True)
