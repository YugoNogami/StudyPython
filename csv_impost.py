#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import csv
import pandas as pd

df = pd.read_csv('./lunch_box.csv', sep=',')
print(df.head(3))
print(df.shape)
print(df.index)
print(df.columns)
print(df.dtypes)

# 任意の列だけ取り出したい場合
print(df[['name', 'kcal']].head())

# 100行目から105行目まで表示したい場合
print (df[100:106])
