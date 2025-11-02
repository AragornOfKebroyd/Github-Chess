import json
import sys
import chess
# this code updates state.json using python-chess

# throws error if
# 1. move not given
# 2. move is invalid or illegal

def main():
    if len(sys.argv) >= 2:
        move = sys.argv[1]
    else:
        raise ValueError("Usage: `python update_board.py <move>`\n e.g python update_board e2e4")

    # read in state
    with open('state.json', 'r') as f:
        state = json.load(f)

    board = chess.Board(state["board"])

    board.push_uci(move)

    # use board.board_fen() for only the board section (not including turn and castling data)
    state["board"] = board.fen()
    state["moves"].append(move)
    state["turn"] = "black" if state["turn"] == "white" else "white"

    with open("state.json", "w") as f:
        json.dump(state, f)


if __name__ == "__main__":
    main() 
