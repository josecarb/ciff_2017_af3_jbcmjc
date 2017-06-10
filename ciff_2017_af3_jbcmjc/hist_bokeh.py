from flask import render_template
import matplotlib.pyplot as plt
import io
import base64
import pandas as pd
from create_lagged_series2 import create_lagged_series2
import datetime
from datetime import datetime
import numpy as np
from matplotlib.pyplot import *


def hist_bokeh(ndias, symbol):
	lags = int(ndias)
	tsret = pd.DataFrame()
	tsret = create_lagged_series2(lags, symbol)
	# datos del histograma
	hist, edges = np.histogram(tsret, bins=10, range=(-0.1,0.1))
	total_muestra = sum(hist)
	hist = hist / float(total_muestra)
	
	img = io.BytesIO()
	# figura bokeh
	#hist_title = symbol + " histogram, lags: " + str(lags)
	#p1 = figure(title = hist_title, background_fill_color="#E8DDCB")
	#p1.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:],fill_color="#036564", line_color="#033649")
	
	#p1.legend.location = "top_left"
	#p1.xaxis.axis_label = '% Earnings'
	#p1.yaxis.axis_label = 'Probability'
	plt.hist(hist)
	plt.savefig(img,format='png')
	img.seek(0)
	print 'grafico_creado'
	#output_file("./templates/stocks.html", title="My Own Bokeh Example")
	#output_file('./templates/histogram.html')
	p1 = base64.b64encode(img.getvalue()).decode()
	return p1