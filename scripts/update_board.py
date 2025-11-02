import json
import sys
import chess
import os
# this code updates state.json using python-chess

# throws error if
# 1. move not given
# 2. move is invalid or illegal
state_path = os.path.join(os.path.dirname(__file__),'..','state.json')


def update_board(from_square: str, to_square: str, promotion=False) -> None:
    uci_move = f"{from_square}{to_square}{'q' if promotion else ''}"

    # read in state
    with open(state_path, 'r') as f:
        state = json.load(f)

    board = chess.Board(state["board"])

    board.push_uci(uci_move)

    # use board.board_fen() for only the board section (not including turn and castling data)
    state["board"] = board.fen()
    state["moves"].append(uci_move)
    state["turn"] = "black" if state["turn"] == "white" else "white"

    with open(state_path, "w") as f:
        json.dump(state, f)


def get_board_after_move(uci_move, cur_fen) -> str:
    board = chess.Board(cur_fen)
    board.push_uci(uci_move)

    return board.fen()


