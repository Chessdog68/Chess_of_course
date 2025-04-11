from flask import Flask, request, jsonify, render_template
import chess
import chess.engine

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  

board = chess.Board()
#   # Initialize the Stockfish engine
engine = chess.engine.SimpleEngine.popen_uci("stockfish/stockfish-windows-x86-64-avx2.exe")  
engine.configure({"Threads": 1, "Hash": 512, "Skill Level": 0})
# moves and setting level

@app.route("/move", methods=["POST"])
def move():
    data = request.get_json()
    move_uci = data.get("move")

    try:
        move = chess.Move.from_uci(move_uci)
        if move not in board.legal_moves:
            return jsonify({"status": "illegal move"}), 400

        board.push(move)

        # Get Stockfish response
        result = engine.play(board, chess.engine.Limit(time=0.1))
        if result.move is None:
            return jsonify({"status": "game over", "ai_move": None}), 200

        board.push(result.move)

        return jsonify({
            "status": "ok",
            "ai_move": result.move.uci()
        })

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
