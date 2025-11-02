from flask import Flask, request, redirect, send_file, Response
import requests
import os
import json
import chess
import chess.svg

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
def click():
    square = request.args.get("sq")
    game = request.args.get("game")

    # game logic
    with open('../state.json', 'r') as f:
        state = json.load(f)

    # get variables
    board = chess.Board(state["board"])

    chess_square = chess.parse_square(square) # chess_square is python chess square object eg: chess.A8
    piece = board.piece_at(chess_square)

    player = state["turn"] # white or black

    if state[player] == "start":
        if piece == None:
            state[player] = "start" # state remains at start as user didn't select valid move
        else:
            state[player] = "selected" # change state to selected to display valid moves
            state["on_select"] = square

            # get legal moves of the square
            for move in board.legal_moves:
                # Filter moves that START at the selected source square
                if move.from_square == chess_square:
                    legal_list.append(chess.square_name(move.to_square))
                    # eg: legal string is something like a4e5c3

            state["legal_list"] = legal_list


    elif state[player] == "selected":
        selected_chess_square = chess.parse_square(state["on_select"])
        selected_piece = board.piece_at(selected_chess_square)

        if state["on_select"] in state["legal_list"]: # user makes a legal move
            # *** call function to update board ***
            # moving FROM state["on_select"]
            # moving TO square
            # these will be strings eg: "e4", not python chess constants

            state[player] = "start"
        else:
            state[player] = "start"


        # reset legal list
        state["legal_list"] = ""


    # write back state into json
    with open('../state.json', 'w') as f:
        json.dump(state, f, indent=4)

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

    with open('../state.json', 'r') as f:
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

    # add green indicator
    if square in legal_list:
        imagename = imagename + 'h'

    imagename = imagename + '.png'

    path = os.path.join(os.getcwd(), "images", imagename)
    return send_file(path, mimetype='image/png')

@app.route('/displayboard')
def display_board():
    with open('state.json', 'r') as f:
        state = json.load(f)
    
    board = chess.Board(state["board"])

    svg = chess.svg.board(
        board
    )

    return Response(svg, mimetype='image/svg+xml')



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
