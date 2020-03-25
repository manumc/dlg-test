#!/usr/bin/env python3

from flask import Flask, render_template, jsonify

app = Flask(__name__)

numbers_to_add = list(range(10_000_001))

@app.route("/")
def welcome():
    """
    Welcome/Landing page for the web app.
    """
    return render_template("welcome.html")

@app.route("/total")
def total():
    """
    Calculate the sum of a list of numbers. (Hardcoded for the sake of this test.)
    Return JSON with the answer.
    """
    return jsonify({"total": sum(numbers_to_add)})
