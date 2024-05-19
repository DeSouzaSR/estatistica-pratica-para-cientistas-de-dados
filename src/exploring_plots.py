#%%
# Imports 
import pandas as pd
from statsmodels import robust
import matplotlib.pyplot as plt

#%%
# Read dataset
state = pd.read_csv('../data/raw-data/state.csv')

#%%
# Quantil
print("Quantiles 0.05, 0.25, 0.5, 0.75, 0.95")
print(state['Murder.Rate'].quantile([0.05, 0.25, 0.5, 0.75, 0.95]))
# %%
# Boxplot for population
ax = (state['Population']/1_000_000).plot.box()
ax.set_ylabel('Population [millions]')
ax.axes.get_xaxis().set_ticks([])
plt.show()
# %%
# Tabela de frequências
binnedPopulation = pd.cut(state['Population'], 10)
print(binnedPopulation.value_counts())
# %%
