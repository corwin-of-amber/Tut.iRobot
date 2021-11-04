from flask import Flask, render_template, request
import logic

app = Flask(__name__, static_url_path="/ui", static_folder="ui")

@app.route("/")
def main_page():
    return render_template('index.html')

from markupsafe import escape

@app.route("/<name>")
def hello(name):
    import json

    J = '{"walls":[[13,7],[11,7],[12,7],[11,6],[11,5],[11,4],[11,3],[11,2],[10,2],[9,2],[8,2],[7,2],[6,2],[6,3],[6,4],[6,5],[6,6],[6,7],[7,7],[7,8],[7,9],[6,9],[6,10],[6,11],[6,12],[7,12],[8,12],[9,12],[10,12],[11,12],[12,12],[13,12],[13,11],[13,10],[13,9],[13,8]]}'
    board = json.loads(J)

    Move, RotateRight = logic.initialize_simulation(board)
    logic.irobot_clean(Move, RotateRight)
    return f"Hello, {escape(name)}!"

@app.route("/json", methods=["POST"])
def get_path():
    print("WE GOT HERE")
    print(request.data)

    import json
    board = json.loads(request.data)

    Move, RotateRight = logic.initialize_simulation(board)
    logic.irobot_clean(Move, RotateRight)

    return "---"