from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

lobby = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_player', methods=['POST'])
def add_player():
    player_name = request.form['player_name']
    lobby.append(player_name)
    return redirect(url_for('lobby', player=player_name))

@app.route('/lobby/<player>')
def lobby(player):
    return render_template('lobby.html', player=player, players=lobby)

if __name__ == '__main__':
    app.run(debug=True)
