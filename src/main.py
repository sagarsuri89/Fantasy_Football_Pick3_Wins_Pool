from sportsipy.nfl.teams import Teams
import numpy as np
import pandas as pd


owner_dataframe = pd.read_excel(r'ThreeTeamAssignments2023.xlsx', sheet_name = 'Sheet1')
listtemp = []
#Update the year here:
for team in Teams(2023):
    listtemp.append([team.abbreviation,team.wins])
columnnames = ["team","wins"]
teamwins_df = pd.DataFrame(listtemp,columns = columnnames)
join_df = pd.merge(owner_dataframe, teamwins_df, left_on = 'team',right_on = 'team', how = 'left')
reduce_df = join_df[['Header','wins']]
rename_df = reduce_df.rename({'Header':'Team'}, axis = 'columns')
agg_df= rename_df.groupby('Team').sum()
summary_df = agg_df.sort_values(by='wins', ascending=False)
print(summary_df)
