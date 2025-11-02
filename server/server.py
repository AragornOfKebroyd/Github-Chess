from flask import Flask, request, redirect, send_file, Response, send_from_directory
import requests
import os
import json
import sys
import chess
import chess.svg
import subprocess, time
# import update_board.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scripts import update_board, generate_board


app = Flask(__name__)

GITHUB_TOKEN = os.environ.get("ACCESS_TOKEN")

state_path = os.path.join(os.path.dirname(__file__),'..','state.json')

@app.route("/")
def hello():
    return "GitHub Chess backend is live!"

@app.route("/move")
def move(): # DEPRICATED
    move = request.args.get("move")
    game = request.args.get("game")
    redirect_url = request.args.get("redirect", "https://github.com/AragornOfKebroyd/Github-Chess")

    # Call GitHub API to trigger repository_dispatch

    # note that this should only be done upon shutting down of the codespace to make sure that it is stored
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
def click(): # state logic
    square = request.args.get("sq")
    current_player = request.args.get("player")
    game = request.args.get("game")
    redirect_url = request.args.get("redirect", f"https://github.com/AragornOfKebroyd/Github-Chess/{current_player}")

    # game logic
    with open(state_path, 'r') as f:
        state = json.load(f)
    # print(state)
    # print(state['board'])

    # get variables
    board = chess.Board(state["board"])
    chess_square = chess.parse_square(square) # chess_square is python chess square object eg: chess.A8
    piece = board.piece_at(chess_square)
    
    player = state["turn"] # white or black

    if player != current_player:
        # do nothing
        print("WRONG PLAYER'S TURN, EXITING WITH NO FURTHER COMPUTATION")
        print(player,current_player) # check working
        return redirect(redirect_url)

    if state[player] == "start":
        print(piece)
        if piece == None:
            state[player] = "start" # state remains at start as user didn't select valid move
        else:
            state[player] = "selected" # change state to selected to display valid moves
            state["on_select"] = square
    
            legal_list = []
    
            # get legal moves of the square
            for move in board.legal_moves:
                # Filter moves that START at the selected source square
                if move.from_square == chess_square:
                    legal_list.append(chess.square_name(move.to_square)) # keep in mind, if we dont have enough info later, change this
                    # eg: legal string is something like ['e3', 'e4']
            print(legal_list)
            state["legal_list"] = legal_list
    
    
    
    elif state[player] == "selected":
        selected_chess_square = chess.parse_square(state["on_select"])
        selected_piece = board.piece_at(selected_chess_square)
    
        # print(state["on_select"], repr(square), state["legal_list"])
    
        if square in state["legal_list"]: # user makes a legal move
            # TODO handle promotions
            uci_move = f"{state['on_select']}{square}"
            state["board"] = update_board.get_board_after_move(uci_move, state["board"])
            state["turn"] = "black" if state["turn"] == "white" else "white"
            state["moves"].append(uci_move)

    
        state[player] = "start"
    
    
        # reset legal list
        state["legal_list"] = []


    # write back state into json
    with open(state_path, 'w') as f:
        json.dump(state, f, indent=4)

    print("HEREHRHEHRHER")
    # update time query tags to avoid caching
    new_html = generate_board.generate_board(current_player)
    with open(os.path.join(os.path.dirname(__file__),'..','play',current_player,'README.html'), 'w') as f:
        f.write(new_html)

    # push to github
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", f"Update {player} board at {time.time()}"], check=True)
    subprocess.run(["git", "pull"], check=True)
    subprocess.run(["git", "push"], check=True)
    print("Pushed board update to GitHub.")

    # read the board state and return
    return redirect(redirect_url)

pieceEnum = {chess.BISHOP: 'b', chess.KING: 'k', chess.KNIGHT: 'n', chess.PAWN: 'p', chess.QUEEN: 'q', chess.ROOK: 'r'}
colourEnum = {chess.BLACK: 'd', chess.WHITE: 'l'}

@app.route("/display", methods=['GET'])
def display():
    square = request.args.get("sq")
    current_player = request.args.get("player")
    game = request.args.get("game")
    
    with open(state_path, 'r') as f:
        state = json.load(f)

    board = chess.Board(state["board"])
    chess_square = chess.parse_square(square)
    piece = board.piece_at(chess_square)
    board_colour = 'd' if (int(square[1]) +ord(square[0])) % 2 == 0 else 'l'

    # find name of png
    if piece == None:
        imagename = 'e'
    else:
        imagename = pieceEnum[piece.piece_type] + colourEnum[piece.color]

    imagename = imagename + board_colour
    # add green indicator for correct player

    player = state["turn"]
    if square in state["legal_list"] and current_player == player:
        imagename = imagename + 'h'

    imagename = imagename + '.png'

    path = os.path.join(os.getcwd(), "images", imagename)
    return send_file(path, mimetype='image/png')

@app.route('/displayboard')
def display_board():
    with open(state_path, 'r') as f:
        state = json.load(f)
    
    board = chess.Board(state["board"])

    svg = chess.svg.board(
        board
    )

    return Response(svg, mimetype='image/svg+xml')



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
