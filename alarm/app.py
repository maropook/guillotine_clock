# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from cron import cron

app = Flask(__name__)


# 関数名は全部違うものにする必要がある

@app.route('/', methods=['GET'])
def get():
    return render_template('index.html', alarm_time=f'')


@app.route('/', methods=['POST'])
def index():
    alarm_time = request.form.get('alarm_time')
    cron.set_job(alarm_time)
    return render_template('index.html', alarm_time=f'{alarm_time}にセットしました。')

@app.route('/test')
def test_index():
    my_dict = {
        'insert_something1': 'views.pyのinsert_something1部分です。',
        'insert_something2': 'views.pyのinsert_something2部分です。',
        'test_titles': ['title1', 'title2', 'title3']
    }
    return render_template('testapp/index.html', my_dict=my_dict)

if __name__ == '__main__':
    app.run("0.0.0.0")
