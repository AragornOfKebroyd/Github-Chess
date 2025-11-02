import json
import sys
import chess
import os

# initialises state.json with the beginning of a game
state_path = os.path.join(os.path.dirname(__file__),'..','state.json')

def main():
    # TODO remove game_id everywhere
    if len(sys.argv) >= 2:
        game_id = sys.argv[1]
    else:
        game_id = "game0"
    # white_player = sys.argv[2] or "Player1"
    # black_player = sys.argv[3] or "Player2"

    board = chess.Board()

    state = {
        "white": "start",  # represents whether player has selected a piece or not
        "black": "start",
        "turn": "white",
        "moves": [],
        "board": board.fen(),
        "on_select": None,  # represents currently selected square
        "legal_list": [],  # allowed moves from 'on_select'
    }

    with open(state_path, "w") as f:
        json.dump(state, f)


if __name__ == "__main__":
    main()

