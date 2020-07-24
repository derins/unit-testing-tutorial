from flask import Flask, render_template, url_for, request
from datetime import datetime
from time_of_day import *


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/schedule', methods=['POST'])
def get_dog_info():
    if request.method == 'POST':

        result = request.form

        name = result['name']
        scheduled_time = result['time']
        color = result['color']

        # for untestable code example
        # time_of_day = get_time_of_day()

        # testable and reuseable code example and more
        time_of_day = get_time_of_day(datetime.datetime.now().time())
        drop_off_time = get_time_of_day(datetime.datetime.strptime(scheduled_time, '%Y-%m-%dT%H:%M'))

    # needed for bad example to work
    # return render_template('schedule.html', name = name, time = scheduled_time, color = color, time_of_day = time_of_day)

    return render_template('schedule.html', name = name, time = scheduled_time, color = color, time_of_day = time_of_day, drop_off_time = drop_off_time)


if __name__ == '__main__':
    app.run(debug=True)
