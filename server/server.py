from flask import Flask, request, redirect
import requests
import os
# from ../scripts/generate_board import generate_board_image

app = Flask(__name__)

GITHUB_TOKEN = os.environ.get("ACCESS_TOKEN")

@app.route("/")
def hello():
    return "GitHub Chess backend is live!"

@app.route("/move")
def move():
    move = request.args.get("move")
    game = request.args.get("game")
    redirect_url = request.args.get("redirect", "https://github.com/AragornOfKebroyd/Github-Chess")

    # Call GitHub API to trigger repository_dispatch
    payload = {"game": game, "move": move}
    response = requests.post(
        "https://api.github.com/repos/AragornOfKebroyd/Github-Chess/dispatches",
        headers={
            "Authorization": f"token {GITHUB_TOKEN}",
            "Accept": "application/vnd.github.everest-preview+json",
        },
        json={"event_type": "make_move", "client_payload": payload},
    )

    print("Status code:", response.status_code)
    print("Response body:", response.text)

    # # update board image
    # assert(False)
    # generate_board_image(fen=state["board"], output_path="../board_image.png")
    
    return redirect(redirect_url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
