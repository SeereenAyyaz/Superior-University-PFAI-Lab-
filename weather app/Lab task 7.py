from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "ee43d0195215301ffbcc0d89f67bd6ff"

@app.route('/', methods=['GET', 'POST'])
def home():
    weather_data = None
    city = None
    error = None

    if request.method == 'POST':
        city = request.form['city']
        if city:
            try:
                url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
                response = requests.get(url)
                data = response.json()

                if data['cod'] == 200:
                    weather_data = {
                        "city": data['name'],
                        "temperature": data['main']['temp'],
                        "description": data['weather'][0]['description'],
                        "humidity": data['main']['humidity'],
                        "wind_speed": data['wind']['speed'],
                        "feels_like": data['main']['feels_like'],
                        "pressure": data['main']['pressure']
                    }
                else:
                    error = "City not found. Please enter a valid city name."
            except Exception as e:
                error = f"Error fetching data: {e}"

    # ✅ make sure this return statement is outside the IF block (aligned with 'if request.method')
    return render_template('index.html', weather=weather_data, city=city, error=error)

if __name__ == '__main__':
    app.run(debug=True)
