from flask import Flask, render_template

app = Flask(__name__)

destinations = [
    "Dubai", "Abu Dhabi", "Azerbaijan", "Bali", "Egypt",
    "Georgia", "Hongkong and Macau", "Malaysia", "Kenya",
    "Maldives", "Mauritius", "Poland", "Singapore", "Thailand"
]

packages = [
    {"name": "Dubai City Tour", "price": "AED 1200", "days": "4 Days", "img": "dubai.jpg"},
    {"name": "Maldives Luxury Trip", "price": "AED 3000", "days": "5 Days", "img": "maldives.jpg"},
    {"name": "Thailand Fun Trip", "price": "AED 1800", "days": "5 Days", "img": "thailand.jpg"},
    {"name": "Kenya Safari", "price": "AED 2500", "days": "6 Days", "img": "kenya.jpg"}
]

@app.route('/')
def home():
    return render_template('index.html', packages=packages, destinations=destinations)

@app.route('/destinations')
def destinations_page():
    return render_template('destinations.html', destinations=destinations)

@app.route('/destination/<path:name>')
def destination_page(name):
    video_name = name.lower().replace(" ", "_") + ".mp4"
    return render_template('destination.html', name=name, video=video_name)

@app.route('/visa')
def visa():
    return render_template('visa.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)