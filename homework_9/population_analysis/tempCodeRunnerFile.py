 = df[['state']].drop_duplicates().sort_values(by='state').reset_index().drop(columns='index')
# df2 = df.groupby('state')[[]].agg({'Salary Band': 'sum'})
# print(df2)