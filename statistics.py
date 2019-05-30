import pandas as pd

season_data = pd.read_csv("Seasons_Stats.csv")
original_df = pd.DataFrame(season_data)

'''
Statistics to use
TS%
TRB%
AST%
STL%
BLK%
TOV% 
'''
# Subtract 1 from TOV because 1 - turnover rate = non turnover rate which is what we want
original_df['TOV%'] = 100 - original_df['TOV%']

#Games minimum reduces skewness in data

df = original_df.query('G > 65 & MP > 2800')

#normalize each column
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

#Repeat Players

for x in range(20):
    print(str(x+1) + ') ' + str(df['Player'][data_sort[x][0]]) + ' ' + str(df['Year'][data_sort[x][0]])+ ' ' + str(data_sort[x][1]))

print('---------------------------')

player_duplicates = []

#No Repeat Players

end = 20
x = 0
count = 1

while end > x:
    cur_player  = df['Player'][data_sort[x][0]]
    if cur_player not in player_duplicates:
        print(str(count) + ') ' + cur_player + ' ' + str(df['Year'][data_sort[x][0]]) + ' ' + str(data_sort[x][1]))
        player_duplicates.append(cur_player)
        count += 1
    else:
        end += 1
    x += 1

