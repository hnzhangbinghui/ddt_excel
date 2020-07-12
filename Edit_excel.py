import re
import xlrd
import xlwt
import  pandas as pd
import numpy as np
def open_excel():
    wk=xlrd.open_workbook(r'C:\Users\LX\Desktop\summary and  details\calculation_details_CCH2020032319144_20200323172913.xlsx')
    sheets=wk.sheet_names()
    print(sheets)
    ws=wk.sheet_by_index(0)
    nrows=ws.nrows
    ncols=ws.ncols
    print('行数：',nrows,'列数：',ncols)
    datarow=ws.row_values(0)
    print('获取第一行的值：',datarow)
    datacol=ws.col_values(0)
    print('获取第一列的值：',datacol)
    print(type(datarow))
    #拼接字符串
    head_text=','.join('%s' %id for id in datarow)
    print(head_text)
    print(type(head_text))
    #re.findall,判断某个字符串是否在字符串当中
    calcu_id=re.findall(datarow[0],head_text)
    print(calcu_id)




















open_excel()