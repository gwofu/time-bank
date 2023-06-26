from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
  return 'Hello, Gwowen!'


@app.route("/user/<name>")
def user():
  return "Hi {{name}}"


if __name__ == "__main__":
  print("I am inside the if now")
  app.run(host="0.0.0.0", debug=True)
