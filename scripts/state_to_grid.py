# --- 1. Image Naming Convention Map ---
# Maps the FEN piece character to the two-letter file prefix.
# Example: 'k' -> 'kd' (King, Dark color) | 'Q' -> 'ql' (Queen, Light color)
FEN_TO_NAME = {
    # Black Pieces (Piece Type + 'd' for Dark/Black color)
    'k': 'kd',
    'q': 'qd',
    'r': 'rd',
    'b': 'bd',
    'n': 'nd',
    'p': 'pd',

    # White Pieces (Piece Type + 'l' for Light/White color)
    'K': 'kl',
    'Q': 'ql',
    'R': 'rl',
    'B': 'bl',
    'N': 'nl',
    'P': 'pl',
}

# --- 2. Empty Square Names ---
EMPTY_LIGHT = 'el.png'  # For an empty light square
EMPTY_DARK = 'ed.png'   # For an empty dark square

def is_dark_square(file_index: int, rank_index: int) -> bool:
    """
    Determines if a square is dark based on its coordinates.
    Standard convention: (File + Rank) is EVEN for a Dark square.
    (File A=0, Rank 1=0, up to File H=7, Rank 8=7)
    """
    # Sum the zero-indexed file and rank. A1 = 0+0 = 0 (Dark if A1 is Dark)
    # The standard convention for an 8x8 grid is that squares where the sum of
    # the coordinates is EVEN are one color, and ODD is the other.
    # We'll assume the common visual layout where A1 is Dark.
    return (file_index + rank_index) % 2 == 0

def generate_image_grid_standalone(fen_string):
    """
    Converts a FEN string into an 8x8 grid of image filenames without the chess module.
    """
    # 1. Strip the FEN to just the piece placement data
    pieces_fen = fen_string.split(' ')[0]

    image_grid = []

    # Initialize rank and file indices
    current_rank_index = 7 # Start at Rank 8

    # The FEN string iterates over the board row-by-row (Rank 8 down to Rank 1)
    for rank_fen_string in pieces_fen.split('/'):
        rank_images = []
        current_file_index = 0 # Start at File A

        # 2. Parse the FEN string for the current rank
        for char in rank_fen_string:
            if char.isdigit():
                # Encountered a number: Skip empty squares
                empty_count = int(char)
                for _ in range(empty_count):
                    # Determine background color for the empty square
                    is_dark = is_dark_square(current_file_index, current_rank_index)
                    bg_suffix = 'd' if is_dark else 'l'

                    filename = EMPTY_DARK if is_dark else EMPTY_LIGHT
                    rank_images.append(filename)
                    current_file_index += 1

            elif char.isalpha():
                # Encountered a piece character
                is_dark = is_dark_square(current_file_index, current_rank_index)
                bg_suffix = 'd' if is_dark else 'l'

                # Get the 2-letter piece/color prefix (e.g., 'kd', 'ql')
                prefix = FEN_TO_NAME.get(char)

                if prefix:
                    filename = f"{prefix}{bg_suffix}.png"
                else:
                    filename = f"unknown_{bg_suffix}.png"

                rank_images.append(filename)
                current_file_index += 1

        image_grid.append(rank_images)
        current_rank_index -= 1 # Move down to the next rank (7 -> 6, etc.)

    return image_grid

# --- Example Usage ---
START_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

if __name__ == "__main__":

    image_grid = generate_image_grid_standalone(START_FEN)

    print("Generated 2D Image Filename Grid (Rank 8 to Rank 1):")
    for row in image_grid:
        print(row)
