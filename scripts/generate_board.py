import chess
import chess.svg
import json
import cairosvg 
from io import BytesIO

STATE_FILE = "../state.json"
IMAGE_PATH = "../board_image.png"

def generate_board_image(output_path: str):
    # ... (FEN loading logic remains the same)
    try:
        with open(STATE_FILE, 'r') as f:
            game_state = json.load(f)
        fen = game_state.get("board", "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKB1R w KQkq - 0 1")
    except Exception:
        fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
        print(f"Using default FEN.")

    try:
        board = chess.Board(fen)
    except ValueError:
        print(f"Error: Invalid FEN string '{fen}'.")
        return

    # 1. Generate the SVG string
    last_move = board.peek() if board.move_stack else None
    svg_data = chess.svg.board(
        board=board,
        lastmove=last_move,
        size=400,
        coordinates=True
    ).encode('utf-8') # Encode the string to bytes

    # 2. Convert SVG bytes to PNG and Save using cairosvg
    try:
        # cairosvg.svg2png converts the byte string directly to a PNG file
        cairosvg.svg2png(bytestring=svg_data, write_to=output_path)
        print(f"Successfully generated and saved board image to {output_path}")

    except Exception as e:
        print(f"A fatal error occurred during SVG to PNG conversion: {e}")

if __name__ == "__main__":
    generate_board_image(IMAGE_PATH)
