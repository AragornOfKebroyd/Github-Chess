import pyperclip
import time

def generate_board(player, clickable):
    if player == "white":
        numrange = range(8, 0, -1)
    else:
        numrange = range(1, 9)

    string = '<p id="jump">Press a piece to show legal moves, then choose or clip off to reset</p>\n'
    url = lambda x: f"https://fictional-orbit-67v7r47r9q9f57wx-5000.app.github.dev/display?game=abc123&sq={x}&player={player}&t={time.time()}"
    clickurl = lambda x: f"https://fictional-orbit-67v7r47r9q9f57wx-5000.app.github.dev/click?game=abc123&sq={x}&player={player}&redirect=https://github.com/AragornOfKebroyd/Github-Chess/tree/main/play/{player}#jump"
    for number in numrange:
        string += "<div>\n"
        for letter in 'abcdefgh':
            square = f"{letter}{number}"
            if clickable:
                string += f'  <a href={clickurl(square)}><img src="{url(square)}"width="64" height="64"/></a>\n'
            else:
                string += f'  <picture><img src="{url(square)}"width="64" height="64"/></picture>\n'
        string += "</div>\n"
    string += '''

    ---

    ### ⚙️ Server Logic Transition

    To move this to **dynamic mode**, you will replace the absolute static image URL (`https://raw.githubusercontent.com/.../FILE.png`) with your server's dynamic endpoint:

    **Static URL (Testing):**
    `https://raw.githubusercontent.com/AragornOfKebroyd/Github-Chess/main/images/kdl.png`

    **Dynamic URL (Production Goal):**
    `https://fictional-orbit-67v7r47r9q9f57wx-5000.app.github.dev/square_img?game=abc123&sq=e8`

    '''
    return string


if __name__ == "__main__":
    player = 'white'
    board_string = generate_board(player)
    pyperclip.copy(board_string)
    print("Board HTML copied to clipboard.")
