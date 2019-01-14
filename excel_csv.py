#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import csv
import pandas as pd

data = pd.read_excel(
  '26-1-18.xlsx', 'sheet1', index_col=None, skiprows=7, skipfooter=2)

data.reset_index()
data.columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

print(data.dtypes)
data.to_csv('data2.csv', encoding='utf-8')
