# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 23:55:16 2020

@author: XuJing3
"""



import pandas as pd
x1=pd.read_csv("car_complain.csv")
df1=pd.DataFrame(x1)
df2=df1.drop('problem', 1).join(df1.problem.str.get_dummies(','))
tags=df2.columns[7:]
df3= df2.groupby(['brand'])[tags].agg(['sum'])
df4=df2.groupby(['brand'])['id'].agg(['count'])
df5=df4.merge(df3,left_index=True, right_index=True, how='left')
df5.reset_index(inplace=True)
df5.sort_values('count',ascending=False)
quary=('A11','sum')
print(df5.sort_values(quary,ascending=False))