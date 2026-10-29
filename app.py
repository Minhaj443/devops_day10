from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from CI - My Python app is live!"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
