from flask import Flask, render_template, request
import joblib
from datetime import datetime

app = Flask(__name__)

# Load trained model
model = joblib.load("model/flood_model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Read input values
        features = [
            float(request.form["MonsoonIntensity"]),
            float(request.form["TopographyDrainage"]),
            float(request.form["RiverManagement"]),
            float(request.form["Deforestation"]),
            float(request.form["Urbanization"]),
            float(request.form["ClimateChange"]),
            float(request.form["DamsQuality"]),
            float(request.form["Siltation"]),
            float(request.form["AgriculturalPractices"]),
            float(request.form["Encroachments"]),
            float(request.form["IneffectiveDisasterPreparedness"]),
            float(request.form["DrainageSystems"]),
            float(request.form["CoastalVulnerability"]),
            float(request.form["Landslides"]),
            float(request.form["Watersheds"]),
            float(request.form["DeterioratingInfrastructure"]),
            float(request.form["PopulationScore"]),
            float(request.form["WetlandLoss"]),
            float(request.form["InadequatePlanning"]),
            float(request.form["PoliticalFactors"])
        ]

        # Prediction
        prediction = model.predict([features])[0]

        probability = round(prediction * 100, 2)

        # Risk Level
        if probability >= 70:
            risk = "🔴 HIGH FLOOD RISK"
            color = "#dc3545"
            advice = "Immediate action is recommended. Stay alert and follow official warnings."
        elif probability >= 40:
            risk = "🟡 MODERATE FLOOD RISK"
            color = "#ff9800"
            advice = "Monitor weather updates and be prepared for possible flooding."
        else:
            risk = "🟢 LOW FLOOD RISK"
            color = "#28a745"
            advice = "Flood risk is currently low. Continue regular monitoring."

        current_date = datetime.now().strftime("%d %B %Y")
        current_time = datetime.now().strftime("%I:%M:%S %p")

        return render_template(
            "index.html",
            prediction=probability,
            risk=risk,
            color=color,
            advice=advice,
            date=current_date,
            time=current_time
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction=None,
            risk="Error",
            color="red",
            advice=str(e)
        )


if __name__ == "__main__":
    app.run(debug=True)