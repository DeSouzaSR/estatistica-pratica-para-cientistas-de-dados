# Imports 
import pandas as pd
from statsmodels import robust

# Read dataset
state = pd.read_csv('../data/raw-data/state.csv')

print('Standard deviation: ', state['Population'].std())
print('IRQ: ', state['Population'].quantile(0.75) - state['Population'].quantile(0.25))
print('MAD: ',  robust.scale.mad(state['Population']))