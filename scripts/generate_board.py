import pyperclip

player="black"

if player == "white":
    numrange = range(8, 0, -1)
else:
    numrange = range(1, 9)

string = ""
url = lambda x: f"https://fictional-orbit-67v7r47r9q9f57wx-5000.app.github.dev/display?game=abc123&sq={x}&player={player}"
clickurl = lambda x: f"https://fictional-orbit-67v7r47r9q9f57wx-5000.app.github.dev/click?game=abc123&to={x}&player={player}&redirect=https://github.com/AragornOfKebroyd/Github-Chess/tree/main/play/black#jump"
for number in numrange:
    string += "<div>\n"
    for letter in 'abcdefgh':
        square = f"{letter}{number}"
        string += f'  <a href={clickurl(square)}><img src="{url(square)}"width="64" height="64"/></a>\n'
    string += "</div>\n"

print(string, "coppied to clipboard")
pyperclip.copy(string)