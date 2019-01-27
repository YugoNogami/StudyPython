#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import csv
import pandas as pd


class Excel:
    def __init__(self, filename):
            self.filename = filename
            self.data = (pd.read_excel(
                        self.filename,
                        index_col=None,
                        encoding="shift_jis")
                        )

    def get_dtypes(self):
        self.data.reset_index()
        self.data.columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        return self.data.dtypes

    def get_value(self, row, column):
        return self.data.iloc[row, column]

    def add_number(self, num1, num2):
        if type(num1) is not int or type(num2) is not int:
            raise ValueError
        result = num1 + num2
        return result
