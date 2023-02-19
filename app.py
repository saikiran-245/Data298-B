import boto3
from flask import Flask, render_template, request
import csv

app = Flask(__name__)

s3 = boto3.resource('s3')
bucket = s3.Bucket('data298b-group5')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/charging_stations_LA', methods=['GET'])
def charging_stations_LA():
    Year = request.args.get('Year')
    stations = []
    for obj in bucket.objects.all():
        if obj.key == 'charging_stations_LA.csv':
            file_content = obj.get()['Body'].read().decode('utf-8').splitlines()
            reader = csv.DictReader(file_content)
            for row in reader:
                if row['Year'] == Year:
                    stations.append(row)
            break
    return {'charging_stations_LA': stations}

if __name__ == '__main__':
    app.run(debug=True)
