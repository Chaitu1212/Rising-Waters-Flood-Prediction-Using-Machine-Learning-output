from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# load trained model
#model = pickle.load(open("model.pkl","rb"))
with open("models/floods.save", "rb") as f:
    model = pickle.load(f)

with open("models/transform.save", "rb") as f:
    transformer = pickle.load(f)

# home page
@app.route("/")
def home():
    return render_template("home.html")

# input page
@app.route("/predictpage")
def predictpage():
    return render_template("index.html")

# prediction logic
@app.route("/predict", methods=["POST"])
def predict():

    # get values from form
    values = [float(x) for x in request.form.values()]
    final = np.array(values).reshape(1,-1)

    # predict
    prediction = model.predict(final)[0]

    # show correct page
    if prediction == 1:
        return render_template("chance.html")
    else:
        return render_template("no chance.html")

# run server
if __name__ == "__main__":
    app.run(debug=True)