import re

import xlrd
import xlwt
import pandas as pd
import numpy as np
df=pd.read_excel(r'C:\Users\LX\Desktop\summary and  details\test_data.xlsx')
'''第一部分：得到对应的行列值，并把他们转换为列表：'''
# print('输出前五行：\n',df.head())
# print('输出后五行：',df.tail())
# print('输出第一行的值:\n',df.loc[0])
# print('输出第一列的值：\n',df['Calculation ID'])
# print('输出列的header(得到的类型是dataframe类型)：\n',df.head(0))
# print('把dataframe类型转换为list列表：\n',df.loc[2].tolist())
# cols_first=df['Calculation ID'].values.tolist()
# print('输出第一列：\n',cols_first)
# cols2=list(df['Calculation ID'].values)
# print(cols2)
# print(type(cols2))
# rows=list(df.loc[0])
# print('把第一行转换为list：\n',type(rows),'\n',rows)
# cols=list(df.head(0))
# print('把列头转换为列表：\n',type(cols),'\n',cols,'\n',cols[0:3])
'''第二部分：对应进行计算'''
#groupby分组函数，返回重构格式的dataframe，特别注意，groupby里面的字段内的数据重构后都会变成索引
#一般和sum（）一起使用
#af.groupby(['name','course'])['score'].sum()#先将af按照namej进行分组，再按照score进行分组，最后将score进行叠加
print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
df_group=df.groupby(['PEP Element','Incentive ID','Payment Flag'])['Revenue'].sum()
print('输出分组之后的值：\n',type(df_group),'\n',df_group)
#特别注意：groupby里面的字段内的数据重构后会变成索引
#使用group之后，pep element是外层索引，incentiveID是外层索引，
print(df_group['ALL PRODUCT MDF'])
print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
'''pandas提供了一个灵活高效的groupby功能，它使你能以一种自然的方式对数据集进行切片、切块、摘要
等操作。根据一个或多个键（可以是函数、数组或DataFrame列名）拆分pandas对象。计算分组摘要统
计，如计数、平均值、标准差，或用户自定义函数。对DataFrame的列应用各种各样的函数。应用组内转换
或其他运算，如规格化、线性回归、排名或选取子集等。计算透视表或交叉表。执行分位数分析以及其他分
组分析。
groupby分组函数：
　　返回值：返回重构格式的DataFrame，特别注意，groupby里面的字段内的数据重构后都会变成索引
　　groupby(),一般和sum()、mean()一起使用
————————————————
版权声明：本文为CSDN博主「brucewong0516」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/brucewong0516/article/details/78768443'''
#将df['Revenue']按照分组键为df['Incentive ID']进pr行分组
grouped=df['Revenue'].groupby(df['Incentive ID'])
print(grouped.mean())
print(grouped.sum())

#可以自定义数组进行分组，举例
'''states=np.array(['Ohio','California','California','Ohio','Ohio'])
years=np.array([2005,2005,2006,2005,2006])
#states第一层索引，years第二层分层索引
print(df['data1'].groupby([states,years]).mean())
California  2005    0.791463
            2006    0.462611
Ohio        2005   -0.764611
            2006    0.077367
Name: data1, dtype: float64
'''

#对df根据PEP Element分组，然后对df剩余数值型的数据运算
dfdf=df.groupby('PEP Element').sum()
print(dfdf)

####特别重要：可以对分组进行迭代
#PEP_value是groupby中PEP Element的值，group是要输出的内容
for PEP_value,group in df.groupby('PEP Element'):
    print('\n',PEP_value,group)
#可以对分组后的内容转换为字典
# print('分组转换为字典：\n',dict(list(df.groupby('PEP Element'))))
print('**********************************')
#groupby默认是在axis=0上进行分组的，通过设置也可以在其他任何轴上进行分组
# print('不同的轴进行分组：：\n',dict(list(df.groupby(df.dtypes,axis=1))))
'''第三部分：对应的查询匹配'''
#按值进行过滤
cond=df['PEP Element']=='ALL PRODUCT'
print('按值进行搜索：\n',df[cond].head())
cond2=(df['PEP Element']=='ALL PRODUCT') & (df['Incentive ID']=='ACC00616495') & (df['Payment Flag']=='Y')
print('多个条件组合筛选df：\n',df[cond2].head()['Calculation ID'])

cond3="Revenue=='1684.800'"
print('另外一种组合查询方法：\n',df.query(cond3).head()['Calculation ID'])
#query 方法，可以直接接受一个查询字符串，查询字符串里面有可以直接用in；

#模糊匹配
cond4=df['PEP Element'].str.startswith('ALL')
print('模糊匹配查询：\n',df[cond4])
cond5=df['PEP Element'].str.contains('PRODUCT',regex=True)
#contains可以用正则表达式
print('模糊匹配查询2：\n',df[cond5].to_csv('mohupipei.csv'))
print('匹配查询并去重：\n',df.drop_duplicates(subset=['PEP Element'],keep='first').to_excel('quchong.xlsx'))

#值范围的查询
print('***********************************')
print('输出revenue的值：\n',df['Revenue'])
cond6="Revenue > 14910"
print(df.query(cond6))


