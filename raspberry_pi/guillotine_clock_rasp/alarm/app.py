# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from cron import cron

app = Flask(__name__)


# ブラウザに画面を表示
@app.route('/', methods=['GET'])
def get():
    return render_template('index.html', alarm_time=f'')

# ブラウザからのデータ取得
@app.route('/', methods=['POST'])
def index():
    alarm_time = request.form.get('alarm_time')
    cron.set_job(alarm_time)
    return render_template('index.html', alarm_time=f'{alarm_time}にセットしました。')


if __name__ == '__main__':
    app.run("0.0.0.0")
