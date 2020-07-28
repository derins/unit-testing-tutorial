from flask import Flask, render_template, url_for, request
from datetime import datetime
from time_of_day1 import *


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/schedule', methods=['POST'])
def get_dog_info():
    if request.method == 'POST':

        result = request.form

        name = result['name']
        scheduled_time = datetime.strptime(result['time'], '%Y-%m-%dT%H:%M')
        color = result['color']

        time_of_day = get_time_of_day(datetime.now().time())
        drop_off_time = get_time_of_day(scheduled_time)

    return render_template('schedule1.html', name = name, time = scheduled_time, color = color, time_of_day = time_of_day, drop_off_time = drop_off_time)


if __name__ == '__main__':
    app.run(debug=True)
