import json
import sys
import chess

# initialises state.json with the beginning of a game

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
        "game": game_id,
        "white_state": "start",  # represents whether player has selected a piece or not
        "black_state": "start",
        "turn": "white",
        "moves": [],
        "board": board.fen()
    }

    with open("state.json", "w") as f:
        json.dump(state, f)


if __name__ == "__main__":
    main()

