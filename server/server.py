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
from scripts import update_board, generate_board, initialise_state


app = Flask(__name__)

GITHUB_TOKEN = os.environ.get("ACCESS_TOKEN")

state_path = os.path.join(os.path.dirname(__file__),'..','state.json')

@app.route("/")
def hello():
    return "GitHub Chess backend is live!"

@app.route("/redirect")
def redirect_route():
    redirect_url = request.args.get("redirect")
    return redirect(redirect_url)

@app.route("/reset")
def reset():
    initialise_state.main()
    redirect_url = request.args.get("redirect")
    return redirect(redirect_url)

@app.route("/click")
def click(): # state logic
    square = request.args.get("sq")
    current_player = request.args.get("player")
    game = request.args.get("game")
    redirect_url = request.args.get("redirect", f"https://github.com/AragornOfKebroyd/Github-Chess#jump")

    # game logic
    with open(state_path, 'r') as f:
        state = json.load(f)

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
            promotion_move_list = []

            # get legal moves of the square
            for move in board.legal_moves:
                # Filter moves that START at the selected source square
                if move.from_square == chess_square:
                    print(move)
                    move_to_square = chess.square_name(move.to_square)
                    # autoqueen
                    print(f"{move.to_square = } {move.promotion = }")
                    if move.promotion is not None:
                        promotion_move_list.append(move_to_square)

                    legal_list.append(move_to_square) # keep in mind, if we dont have enough info later, change this
                    # eg: legal string is something like ['e3', 'e4']
            state["legal_list"] = legal_list
            state["prom_list"] = promotion_move_list
            print(f"{state['prom_list'] = }")


    elif state[player] == "selected":
        selected_chess_square = chess.parse_square(state["on_select"])
        selected_piece = board.piece_at(selected_chess_square)

        # print(state["on_select"], repr(square), state["legal_list"])

        if square in state["legal_list"]: # user makes a legal move
            print(square)
            uci_move = f"{state['on_select']}{square}{'q' if square in state['prom_list'] else ''}"
            state["board"] = update_board.get_board_after_move(uci_move, state["board"])
            state["turn"] = "black" if state["turn"] == "white" else "white"
            state["moves"].append(uci_move)
            state[player] = "start"

            # reset legal list
            state["legal_list"] = []
        else:
            state[player] = "selected" # change state to selected to display valid moves
            state["on_select"] = square

            legal_list = []
            promotion_move_list = []

            # get legal moves of the square
            for move in board.legal_moves:
                # Filter moves that START at the selected source square
                if move.from_square == chess_square:
                    print(move)
                    move_to_square = chess.square_name(move.to_square)
                    # autoqueen
                    print(f"{move.to_square = } {move.promotion = }")
                    if move.promotion is not None:
                        promotion_move_list.append(move_to_square)

                    legal_list.append(move_to_square) # keep in mind, if we dont have enough info later, change this
                    # eg: legal string is something like ['e3', 'e4']
            state["legal_list"] = legal_list
            state["prom_list"] = promotion_move_list
            print(f"{state['prom_list'] = }")

    # write back state into json
    print(state)
    with open(state_path, 'w') as f:
        json.dump(state, f, indent=4)


    prev_move = state["moves"][-1] if len(state["moves"]) > 0 else "-"
    board = chess.Board(state["board"])
    
    black_html = generate_board.generate_board('black', state["turn"] == "black", prev_move, board.is_game_over()) # only clickable for the current player
    with open(os.path.join(os.path.dirname(__file__),'..','play','black','README.md'), 'w') as f:
        f.write(black_html)

    white_html = generate_board.generate_board('white', state["turn"] == "white", prev_move, board.is_game_over()) # only clickable for the current player
    with open(os.path.join(os.path.dirname(__file__),'..','play','white','README.md'), 'w') as f:
        f.write(white_html)



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

    # win logic
    if board.is_game_over():
        if board.turn == chess.WHITE:
            if current_player == "white":
                image_pref = "lose"
            else:
                image_pref = "win"
        elif board.turn == chess.BLACK:
            if current_player == "black":
                image_pref = "lose"
            else:
                image_pref = "win"

        if current_player == "black":
            square = square[0] + str(9 - int(square[1])) # flip square for black view

        imagename = image_pref + square + ".png"
        path = os.path.join(os.getcwd(), image_pref, imagename)

    else:
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
