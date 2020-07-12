# coding:utf-8
import xlrd
def get_data(filename,sheetnum):
    path= 'test_excel.xlsx'
    book_data = xlrd.open_workbook(path)   #打开文件，生成对象
    book_sheet = book_data.sheet_by_index(0)   #打开对应的sheet，生成对象
    rows_num = book_sheet.nrows  #总行数
    print('总行数：',rows_num)
    rows0 = book_sheet.row_values(0)  # 第一行的各个名称作为字典的键
    print(rows0)   #得到第一行的列头的值
    rows0_num = len(rows0)  # 列数
    list = []
    for i in range(1, rows_num):
        rows_data = book_sheet.row_values(i)  # 获取每一行的值作为列表
        print(rows_data)
        rows_dict = {}
        for y in range(0, rows0_num):  # 将每一列的值和每一行的值对应起来
            rows_dict[rows0[y]] = rows_data[y]
        list.append(rows_dict)
    return list
if __name__ == '__main__':
    print(get_data('',1))
