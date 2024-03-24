from flask import Flask, render_template, request
import requests
app = Flask(__name__) # create an app instance

@app.route("/")
def home():
    return render_template("index.html")
    
@app.route("/weatherapp", methods=["POST", "GET"])
def get_weather():
    url = "https://api.openweathermap.org/data/2.5/weather"
    apikey="85d87b46d6b3f25cac34477f3a56c918"
    units = request.form.get("units")
    if units == "Celsius":
        units = "metric"
    elif units == "Fahrenheit":
        units = "imperial"
    params = {
        "q": request.form.get("city"),
        "appid": apikey,
        "units": units
    }
    response = requests.get(url, params=params).json()
    city = response['name']
    temperature = response['main']['temp']
    humidity = response['main']['humidity']
    return render_template('result.html', city=city, temperature=temperature, humidity=humidity)

if __name__ == "__main__": # on running python app.py
    app.run(host="0.0.0.0", port= "5000") # run the flask app