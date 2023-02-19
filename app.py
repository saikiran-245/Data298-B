from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/charging_stations_LA', methods=['GET'])
def charging_stations_LA():
    Year = request.args.get('Year')
    stations = []
    with open('charging_stations_LA.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Year'] == Year:
                stations.append(row)
    return {'charging_stations_LA': stations}

if __name__ == '__main__':
    app.run(debug=True)
