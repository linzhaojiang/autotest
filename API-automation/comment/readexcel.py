#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/19 3:59 下午
# @Name    : peilun
# @File    : readexcel.py
# @Software: PyCharm
import os
import xlrd
from comment.log import *

'''
    读取Excel 测试用例 并将用例dict组合成list
'''


def read_exce(rule=".xlsx"):
    try:
        filename = "../casefile/case.xlsx"
        if filename.endswith(rule):
            wb = xlrd.open_workbook(filename)
            ws = wb.sheet_by_name('Esat')

            all_cases = []

            for r in range(1, ws.nrows):
                case_data = {}
                for c in range(ws.ncols):
                    data_value = ws.cell_value(r, c)
                    case_data[ws.cell_value(0, c)] = data_value
                # all_cases[ws.cell_value(r,0)]=case_data
                # 将返回的dict装入list
                all_cases.append(case_data)
            return all_cases

    except Exception as e:
        errorMsg = str(e)
        log.error("文件格式异常：%s" % errorMsg)





case = read_exce()

