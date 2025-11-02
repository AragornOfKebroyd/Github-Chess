from PIL import Image

def split_chessboard(image_path):
    img = Image.open(image_path)
    tile_size = 90  # each square is 90x90 in a 720x720 image

    files = []

    # Chess board columns a-h
    cols = "abcdefgh"
    # Rows 8 down to 1
    rows = "87654321"

    for r_index, row in enumerate(rows):
        for c_index, col in enumerate(cols):
            left = c_index * tile_size
            top = r_index * tile_size
            right = left + tile_size
            bottom = top + tile_size

            tile = img.crop((left, top, right, bottom))
            filename = f"lose{col}{row}.png"
            tile.save(filename)
            files.append(filename)

    print("Saved tiles:")
    print("\n".join(files))


# Example usage
split_chessboard("lose.png")  # Replace input.png with your 720x720 image
