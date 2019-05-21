import pandas as pd
import numpy as np
season_data = pd.read_csv("/Users/graghu/Desktop/Coding Workspaces/training pages/nba-stats/Seasons_Stats.csv")
print(season_data[0:5])

df = pd.DataFrame(season_data)
# dictionary of medians
category_medians = df.median()
# dictionary of standard deviations
category_sds = df.std()

print(df.max())