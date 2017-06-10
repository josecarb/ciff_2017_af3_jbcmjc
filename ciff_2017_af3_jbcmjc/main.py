# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, jsonify
import pandas.io.sql as sql
import sqlite3
import platform
from datetime import datetime

import numpy as np
import pandas as pd
import json
#from pandas.io.data import DataReader
from pandas_datareader import data, wb
from sklearn.linear_model import LogisticRegression
from sklearn.lda import LDA
from sklearn.qda import QDA

from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file

from scipy.stats import norm

from hist_bokeh import hist_bokeh
from hist_json import hist_json

app = Flask(__name__)

@app.route('/')

def main():

	p1 = hist_bokeh (5,'GOOG')
	p2 = hist_json (5,'GOOG')
	return render_template('histogram.html',p1=p1,p2=p2)


if __name__ == '__main__':
    app.run(
	#host="0.0.0.0",
        #port=int("80")
#        ,	processes=9
debug=True
    )
