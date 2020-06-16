# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 23:32:00 2020

@author: XuJing3
"""

import numpy as np
from pandas import DataFrame
score = {'语文': [68, 95, 98, 90, 80],
        '数学': [65, 76, 86, 88, 90],
        '英语': [30, 98, 88, 77, 90]
        }
df = DataFrame(score,
               index=['张飞', '关羽', '刘备', '典韦', '许褚']
            )
df.index.name = '姓名'
print(df)

print(df.describe().loc[['mean', 'max', 'min', 'std']])
print(np.var(df))


df['总分'] = df.sum(axis=1)
print(df.sort_values(by='总分', ascending=False))