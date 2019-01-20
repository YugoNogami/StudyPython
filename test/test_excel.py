# coding:utf-8

import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../src')
import excel


class TestExcel(object):
    def test_add_number(self):
        test_excel = excel.Excel('./data/26-1-18.xlsx')
        assert test_excel.add_number(50, 10)== 60

    def test_get_value(self):
        test_excel = excel.Excel('./data/26-1-18.xlsx')
        assert test_excel.get_value(10,0) ==  u'島部'
