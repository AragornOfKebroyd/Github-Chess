from flask import Flask, request, redirect, send_file
import requests
import os
import json
import chess

app = Flask(__name__)

GITHUB_TOKEN = os.environ.get("ACCESS_TOKEN")

@app.route("/")
def hello():
    return "GitHub Chess backend is live!"

@app.route("/move")
def move():
    move = request.args.get("move")
    game = request.args.get("game")
    redirect_url = request.args.get("redirect", "https://github.com/AragornOfKebroyd/Github-Chess")

    # Call GitHub API to trigger repository_dispatch
    payload = {"game": game, "move": move}
    response = requests.post(
        "https://api.github.com/repos/AragornOfKebroyd/Github-Chess/dispatches",
        headers={
            "Authorization": f"token {GITHUB_TOKEN}",
            "Accept": "application/vnd.github.everest-preview+json",
        },
        json={"event_type": "make_move", "client_payload": payload},
    )

    print("Status code:", response.status_code)
    print("Response body:", response.text)

    # # update board image
    # assert(False)
    # generate_board_image(fen=state["board"], output_path="../board_image.png")
    
    return redirect(redirect_url)

@app.route("/click")
def click():
    square = request.args.get("sq")
    game = request.args.get("game")
    redirect_url = request.args.get("redirect", "https://github.com/AragornOfKebroyd/Github-Chess/play/white")

    # read the board state and return
    return redirect(redirect_url)

pieceEnum = {chess.BISHOP: 'b', chess.KING: 'k', chess.KNIGHT: 'n', chess.PAWN: 'p', chess.QUEEN: 'q', chess.ROOK: 'r'}
colourEnum = {chess.BLACK: 'd', chess.WHITE: 'l'}

@app.route("/display", methods=['GET'])
def display():
    # return an image grid square
    square = request.args.get("sq")
    
    game = request.args.get("game")

    with open('state.json', 'r') as f:
        state = json.load(f)
    
    board = chess.Board(state["board"])
    chess_square = chess.parse_square(square)
    piece = board.piece_at(chess_square)
    board_colour = 'd' if (int(square[1]) +ord(square[0])) % 2 == 0 else 'l'

    if piece == None:
        imagename = 'e' + board_colour + '.png'
    else:
        imagename = pieceEnum[piece.piece_type] + colourEnum[piece.color] + board_colour + '.png'

    path = os.path.join(os.getcwd(), "images", imagename)
    return send_file(path, mimetype='image/png')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
