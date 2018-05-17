import pandas as pd

dt = pd.read_csv(".")
dt.columns
dt.groupby('Primary Type').max()
