#!/usr/bin/env python
# coding:utf-8
# Created by Jeff on 2016/7/17 14:54
from flask import Flask, render_template
from livereload import Server

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index1.html', title="<h1>Hello World</h1>")


if __name__ == '__main__':
    live_server = Server(app.wsgi_app)
    live_server.watch('**/*.*')
    live_server.serve(open_url=True)
