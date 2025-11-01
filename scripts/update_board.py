# import chess
import json
import sys
import chess
# this code updates state.json using python-chess

def main():
    game_id = sys.argv[1]
    move = sys.argv[2]

    # read in state
    with open('state.json', 'r') as f:
        state = json.load(f)

    board = chess.Board(state["board"])

    board.push_uci(move)

    # for testing
    # state["board"] = board.fen()
    # state["board"] = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    
    state["moves"].append(move)
    state["turn"] = "black" if state["turn"] == "white" else "white"

    with open("state.json", "w") as f:
        json.dump(state, f)

    # assert(False)
    # generate_board_image(fen=state["board"], output_path="../board_image.png")

main()    
