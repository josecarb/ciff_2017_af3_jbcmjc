import pandas as pd
import datetime

import pandas_datareader
from pandas_datareader import data, wb
import numpy as np

def create_lagged_series2(ndias, symbol):

    lags = int(ndias)
    tsret = pd.DataFrame()

    # Obtain stock information from google Finance
    days_calc = 365
    start_date = datetime.datetime.today() - datetime.timedelta(days=days_calc)
    end_date = datetime.datetime.today()
    ts = data.DataReader(symbol, "google", start_date, end_date)

    # Create the new lagged DataFrame
    tslag = pd.DataFrame(index=ts.index)
    tslag["Low"] = ts["Low"]

    # Create the shifted lag series of prior trading period close values
    for i in range(0, lags+1):
         tslag["LagHigh%s" % str(i)] = ts["High"].shift(i)

    # Create the returns DataFrame
    tsret = pd.DataFrame(index=tslag.index)
    for i in xrange(0,lags+1):
        tsret["Lag%s" % str(i)] = (tslag["Low"]-tslag["LagHigh%s" % str(i)] ) / (tslag["LagHigh%s" % str(i)])

    return tsret

