from flask import Flask, render_template, request
from railway import Railway

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        train_no = request.form["train_no"]
        time = request.form["departure_time"]
        source = request.form["source"]
        destination = request.form["destination"]
        railway = Railway(train_no, time, source, destination)
        action = request.form["action"]
        if action == "Book":
            result = railway.book()
        elif action == "Status":
            result = railway.status()
        elif action == "Fare":
            result = railway.fare()
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
