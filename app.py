from flask import Flask, render_template, jsonify
from snake_game import SnakeGame  
app = Flask(__name__)

snake_game = SnakeGame()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_game_state')
def get_game_state():
    game_state = snake_game.get_game_state()
    return jsonify(game_state)

if __name__ == '__main__':
    app.run(debug=True)
