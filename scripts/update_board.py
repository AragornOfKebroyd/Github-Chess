import chess
import json
import sys
from generate_board import generate_board_image # generate board svg image function
# this code updates state.json using python-chess

def main():

    game_id = sys.argv[1]
    move = sys.argv[2]

    # read in state
    with open('state.json', 'r') as f:
        state = json.load(f)

    board = chess.Board(state["board"])

    board.push_uci(move)

    state["board"] = board.fen()
    state["moves"].append(move)
    state["turn"] = "black" if state["turn"] == "white" else "white"

    with open("state.json", "w") as f:
        json.dump(state, f)
    
    generate_board_image(fen=state["board"], output_path="../board_image.png")

main()    
