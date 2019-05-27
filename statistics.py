import pandas as pd

season_data = pd.read_csv("Seasons_Stats.csv")

original_df = pd.DataFrame(season_data)

'''Statistics to use
TS%
TRB%
AST%
STL%
BLK%
TOV% (do 1-TOV%)
'''
# Subtract 1 from TOV because 1 - turnover rate = non turnover rate which is what we want
original_df['TOV%'] = 100 - original_df['TOV%']

#Games minimum reduces skewness in data
games_minimum = original_df['G'] > 30

df = original_df[games_minimum]

TS_normalized = (df['TS%'] - df['TS%'].mean())/df['TS%'].std()
TRB_normalized = (df['TRB%'] - df['TRB%'].mean())/df['TRB%'].std()
AST_normalized = (df['AST%'] - df['AST%'].mean())/df['AST%'].std()
STL_normalized = (df['STL%'] - df['STL%'].mean())/df['STL%'].std()
BLK_normalized = (df['BLK%'] - df['BLK%'].mean())/df['BLK%'].std()
TOV_normalized = (df['TOV%'] - df['TOV%'].mean())/df['TOV%'].std()

#Putting all normalized values into a data frame
df_normalized = pd.concat([TS_normalized, TRB_normalized, AST_normalized, STL_normalized, BLK_normalized, TOV_normalized], axis=1)

player_ratings = {}

for index, row in df_normalized.iterrows():
    player_ratings[index] = (row['TS%'] + row['TRB%'] + row['AST%'] + row['STL%'] + row['BLK%'] + row['TOV%'])/6

data_sort = sorted(player_ratings.items(), key=lambda kv: kv[1])
data_sort.reverse()

for x in range(30):
    print(str(df['Player'][data_sort[x][0]]) + ' ' + str(df['Year'][data_sort[x][0]])+ ' ' + str(data_sort[x][1]))
