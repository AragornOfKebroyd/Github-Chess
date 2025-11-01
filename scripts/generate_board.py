import chess
import chess.svg
import json
from PIL import Image
from io import BytesIO
import os

# --- Configuration ---
STATE_FILE = "state.json"
IMAGE_PATH = "board_image.png"

def generate_board_image(output_path: str):
    """
    Reads the FEN from state.json, generates the board image, and saves it.
    """
    try:
        # 1. Read the FEN from state.json
        with open(STATE_FILE, 'r') as f:
            game_state = json.load(f)
        
        fen = game_state.get("board", "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
        print(f"Read FEN: {fen}")

    except FileNotFoundError:
        print(f"Error: {STATE_FILE} not found. Using starting position.")
        fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {STATE_FILE}.")
        return

    try:
        board = chess.Board(fen)
    except ValueError:
        print(f"Error: Invalid FEN string '{fen}'.")
        return

    # 2. Generate the SVG
    last_move = board.peek() if board.move_stack else None
    
    svg_data = chess.svg.board(
        board=board,
        lastmove=last_move,
        size=400, 
        coordinates=True
    )

    # 3. Convert SVG to PNG and Save
    try:
        # Requires the Pillow library with SVG/cairo support
        img = Image.open(BytesIO(svg_data.encode('utf-8')))
        img.save(output_path, "PNG")
        print(f"Successfully generated and saved board image to {output_path}")

    except Exception as e:
        print(f"An error occurred during image generation (often due to missing 'cairo' dependency): {e}")

if __name__ == "__main__":
    generate_board_image(IMAGE_PATH)
