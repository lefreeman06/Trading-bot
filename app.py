from flask import Flask, request
app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("🚀 Signal reçu :", data)
    return {"status": "reçu"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
