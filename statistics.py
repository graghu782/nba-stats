import pandas as pd
season_data = pd.read_csv("Seasons_Stats.csv")
import numpy as np
print(season_data[0:5])

df = pd.DataFrame(season_data)
# dictionary of medians
category_medians = df.median()
# dictionary of standard deviations
category_sds = df.std()

