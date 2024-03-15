from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__, template_folder="../html")

lobby = []

@app.route('/')
def index():
    return Flask.render_templar('index.html')

@app.route('/add_player', methods=['POST'])
def add_player():
    player_name = request.form['player_name']
    lobby.append(player_name)
    return redirect(url_for('lobby', player=player_name))

joueurs = [{"Joueur1"},{"Joueur2"}, {"Joueur3"}, {"Joueur4"}]

@app.route('../html/lobby.html')
def lobby():
    return render_template('../html/lobby.html', joueurs=joueurs)

if __name__ == '__main__':
    app.run(debug=True)