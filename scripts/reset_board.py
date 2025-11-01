import chess
import json
board = chess.Board()

with open('state.json', 'r') as f:
    state = json.load(f)


