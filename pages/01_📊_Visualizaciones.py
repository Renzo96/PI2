import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import yfinance as yf
import numpy as np
from pandas_datareader import data as pdr
import pyfolio as pf
import pandas_datareader.data as web

import streamlit as st
import numpy as np
import pandas as pd
import yfinance as yf
from scipy.optimize import minimize

# Define the portfolio
portfolio = ['ODFL','MNST','AZO','UNH','ORLY','ACGL','WEC','CHD','NEE','LMT']

# Download the data from Yahoo Finance
prices = yf.download(portfolio, start="2012-01-01", end="2022-03-28")['Adj Close']

# Calculate the log returns
returns = np.log(prices / prices.shift(1))

# Define the objective function
def objective(weights):
    global returns
    port_return = np.sum(returns.mean() * weights) * 252
    port_volatility = np.sqrt(np.dot(weights.T, np.dot(returns.cov() * 252, weights)))
    sharpe_ratio = port_return / port_volatility
    return -sharpe_ratio

# Define the constraints
def constraints(weights):
    return np.sum(weights) - 1

bounds = [(0, 1)] * len(portfolio)
constraints = {'type': 'eq', 'fun': constraints}

# Initialize the weights
weights = np.ones(len(portfolio)) / len(portfolio)

# Calculate the efficient frontier
returns_range = np.linspace(np.min(returns.mean()), np.max(returns.mean()), 100)
frontier_volatility = []
frontier_return = []
for target_return in returns_range:
    cons = [{'type': 'eq', 'fun': lambda x: np.sum(x) - 1},
            {'type': 'eq', 'fun': lambda x, t: np.sum(returns.mean() * x) * 252 - t, 'args': (target_return,)}]
    res = minimize(objective, weights, method='SLSQP', bounds=bounds, constraints=cons)
    frontier_volatility.append(res['fun'])
    frontier_return.append(target_return)

# Plot the efficient frontier
st.line_chart(pd.DataFrame({'returns': frontier_return, 'volatility': frontier_volatility}))
