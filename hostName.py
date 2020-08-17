#!/usr/bin/env python

import os,socket
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hostname():
    return "I am on {}".format(socket.gethostname())

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")