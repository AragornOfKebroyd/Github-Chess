import json
import sys
import chess
import os
from . import generate_board
import subprocess
import time

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
        "legal_list": [],
        "moves": [],
        "board": board.fen(),
        "on_select": None,  # represents currently selected square
        "prom_list": [],  # allowed moves from 'on_select'
    }

    with open(state_path, "w") as f:
        json.dump(state, f, indent=4)

    black_html = generate_board.generate_board('black', False, "-", False)
    with open(os.path.join(os.path.dirname(__file__),'..','play','black','README.md'), 'w') as f:
        f.write(black_html)

    white_html = generate_board.generate_board('white', True, "-", False)
    with open(os.path.join(os.path.dirname(__file__),'..','play','white','README.md'), 'w') as f:
        f.write(white_html)

    # push to github
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", f"Update boards at {time.time()}"], check=True)
    subprocess.run(["git", "pull"], check=True)
    subprocess.run(["git", "push"], check=True)


if __name__ == "__main__":
    main()

