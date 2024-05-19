#%%
# Imports 
import pandas as pd
import numpy as np
from scipy.stats import trim_mean
import wquantiles

#%%
# Read dataset
state = pd.read_csv('../data/raw-data/state.csv')

#%%
# Print mean, trim_mean and median
print("Population mean: ", state['Population'].mean())
print("Trim population mean: ", trim_mean(state['Population'], 0.1))
print("Population median: ", state['Population'].median())

#%%
# weighted median and mean
print("Weighted mean: ", np.average(state['Murder.Rate'], weights=state['Population']))
#%%
#  package wquantiles: https://pypi.org/project/wquantiles/
print("Weighted median: ", wquantiles.median(state['Murder.Rate'], weights=state['Population']))



