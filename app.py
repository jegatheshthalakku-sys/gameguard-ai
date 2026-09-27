from flask import Flask, render_template, request
import joblib

from toxicity import detect_toxicity
from report_generator import generate_report

app = Flask(__name__)

model = joblib.load("churn_model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    matches = float(request.form["matches"])
    session = float(request.form["session"])
    days = float(request.form["days"])
    kills = float(request.form["kills"])
    winrate = float(request.form["winrate"])

    prediction = model.predict([[
        matches,
        session,
        days,
        kills,
        winrate
    ]])[0]

    probability = model.predict_proba([[
        matches,
        session,
        days,
        kills,
        winrate
    ]])[0][1]

    if prediction == 1:
        result = "High Churn Risk"
    else:
        result = "Low Churn Risk"

    return render_template(
        "index.html",
        churn_result=result,
        churn_probability=round(probability * 100, 2)
    )


@app.route("/toxicity", methods=["POST"])
def toxicity():

    player_id = request.form["player_id"]
    message = request.form["message"]

    result = detect_toxicity(message)

    report = ""

    if result["toxic"]:
        report = generate_report(
            player_id,
            message,
            result["words"]
        )

    return render_template(
        "index.html",
        toxicity_result=result,
        report=report
    )


if __name__ == "__main__":
    app.run(debug=True)