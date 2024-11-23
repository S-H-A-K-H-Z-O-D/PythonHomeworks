import pandas as pd
import numpy as np
import sqlite3

with sqlite3.connect('population.db') as con:
    df = pd.read_sql('select * from population', con=con)

dfState = df[['state']].drop_duplicates().sort_values(by='state').reset_index(drop=True)

df2 = df.groupby('state')[['salary']].sum()

totalSalary = df['salary'].sum()

df2['persentage'] = (df2['salary'] / totalSalary) * 100

df2['Avarage Salary'] = df.groupby('state')[['salary']].mean()

print(df2)