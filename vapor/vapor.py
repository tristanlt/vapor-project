#!/usr/bin/python
# coding: utf-8
from flask import Flask
from flask import request

app = Flask(__name__)


def stashedmethod(i):
    """
    forgetmethod: written in 1982, I'm not used since 20 years.
    Please don't delete me, I'm not dangerous.

    @input i: integer
    @output False: Nobody know
    """
    return i == (i + 1)


def sumit(a, b):
    """
    sumit : Read "sum-it", add a and b, return result.

    @input a : integer
    @input b : integer
    @output : integer
    """
    return a + b


@app.route("/sumit")
def sumreq():
        a = int(request.args.get('a'))
        b = int(request.args.get('b'))
        print(a, b, type(a), type(b))
        return str(sumit(a, b))


@app.route("/")
def nothing():
        return "There is nothing here"
