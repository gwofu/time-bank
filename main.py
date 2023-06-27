from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    "id": 1,
    "title": "Data Analyst",
    "location": "Chicago, IL",
    "salary": "72000"
  },
  {
    "id": 2,
    "title": "Software Engineer",
    "location": "Chicago, IL",
    "salary": "102000"
  },
  {
    "id": 3,
    "title": "Backend Developer",
    "location": "Chicago, IL",
    "salary": "82000"
  },
  {
    "id": 4,
    "title": "Frontend Developer",
    "location": "Chicago, IL",
    "salary": "72000"
  },
  {
    "id": 5,
    "title": "Data Developer",
    "location": "Hoffman Estates, IL"
  }    
]


@app.route("/")
def index():
  return render_template("home.html", jobs=JOBS, company_name="Gwo Fu")

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


@app.route("/user/<name>")
def user():
  return "Hi {{name}}"


if __name__ == "__main__":
  print("I am inside the if now")
  app.run(host="0.0.0.0", debug=True)
