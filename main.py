#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
import json
app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080,debug=True)

