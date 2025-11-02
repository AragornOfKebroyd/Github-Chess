import pyperclip
import time
import os

def generate_board(player, clickable, last_move):
    if player == "white":
        numrange = range(8, 0, -1)
    else:
        numrange = range(1, 9)
    
    # read in template
    with open(os.path.join(os.path.dirname(__file__), 'interface_template.txt'), 'r') as f:
        content = f.read()
    
    url = lambda x: f"https://fictional-orbit-67v7r47r9q9f57wx-5000.app.github.dev/display?game=abc123&sq={x}&player={player}&t={time.time()}"
    clickurl = lambda x: f"https://fictional-orbit-67v7r47r9q9f57wx-5000.app.github.dev/click?game=abc123&sq={x}&player={player}&redirect=https://github.com/AragornOfKebroyd/Github-Chess/tree/main/play/{player}#jump"
    
    board_string = ""
    for number in numrange:
        board_string += "<div>\n"
        for letter in 'abcdefgh':
            square = f"{letter}{number}"
            if clickable:
                board_string += f'  <a href={clickurl(square)}><img src="{url(square)}"width="64" height="64"/></a>\n'
            else:
                board_string += f'  <picture><img src="{url(square)}"width="64" height="64"/></picture>\n'
        board_string += "</div>\n"

    content = content.replace("{CHESS_BOARD}", board_string)
    content = content.replace("{CURRENT_PLAYER}", player.capitalize())
    content = content.replace("{LAST_MOVE}", last_move)
    return content


if __name__ == "__main__":
    player = 'white'
    board_string = generate_board(player)
    pyperclip.copy(board_string)
    print("Board HTML copied to clipboard.")
