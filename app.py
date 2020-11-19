from boggle import Boggle
from flask import Flask, render_template, jsonify, redirect, flash, session, request

app = Flask(__name__)
app.config["SECRET_KEY"] = "fuiasjfh488hffgii94"
boggle_game = Boggle()


@app.route("/")
def main_page():
    board = boggle_game.make_board()
    session['board'] = board
    high_score = session.get("high_score", 0)
    num_plays = session.get("num_plays", 0)
    
    return render_template("index.html", board=board, high_score=high_score, num_plays=num_plays)

@app.route("/validate-word")
def validate_word():
    """Check if word is valid in the provided dictionary."""
    word = request.args["word"]
    board = session["board"]
    response = boggle_game.check_valid_word(board, word)
    
    return jsonify({'result': response})

