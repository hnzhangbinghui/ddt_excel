#参考URL：https://baijiahao.baidu.com/s?id=1640210921068132609&wfr=spider&for=pc
import re

import xlrd
import xlwt
import  pandas as pd
import numpy as np
df=pd.read_excel(r'C:\Users\LX\Desktop\summary and  details\test_data.xlsx')
#read_excel的参数比较多，比如sheet_name，是读取那个工作表；
print(df)
print('输出各个字段的类型：\n',df.dtypes)
#筛选表格中的列
# heade_df=df.head(0)
# print(heade_df)
# print(type(heade_df))
# df_gender=df[['Calculation ID', 'Incentive ID',  'PEP Element', 'Revenue', 'Revenue_HWSW', 'Revenue_Services', 'Revenue(Local)','Measure Flag', 'Payment Flag']]
# print(df_gender)
# df_gender_re=df_gender[df_gender.notnull()]  #出去缺失值
print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
#1、按照位置筛选，输出对应的行，筛选第2到5行；
print('第2-5行的数据：\n',df.loc[2:5])
print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
#2、输出对应行列的单个值
rc_val=df.loc[[0],['Calculation ID']]
print('第一行第calculationID列的值：\n',rc_val)  #此时输出的是dfFrame格式的值
val=np.array(rc_val)
print('得到具体的字段值：',val.tolist())
print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
#2、输出特定行，列的值
print('输出特定行的值：\n',df.loc[1])
print('输出某列的值：\n',df['Calculation ID'])
print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
#3、输出某列大于列值大于某值的内容
arr1=df[df['Revenue']>131911]
print('输出Revenue大于10000的值：\n',arr1)
print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
print('输出符合条件的部分字段:\n',arr1['Calculation ID'],arr1['Revenue'])
print(type(arr1))
print('获得符合条件的索引值：\n',df[df['Revenue']>131911].index.tolist())

#4、获取符合条件行的其他列的值，可以考虑把要取的行设为索引
# df=df.set_index('PEP Element')
# print('以PEP Element为索引的数据：\n',df)
# #获取对应航索引
# result=df[df['Revenue']>131911].index.tolist()
# print('更换索引之后的df：\n',df)
# print('获得根据pep element做为索引的符合条件的索引的值：\n',result)

#也可以不改变索引，直接获取过滤后DataFrame中的特定列：
df1=df[df['Measure Flag']=='Y']['Revenue']
print('输出measure flag为Y时的Revenue的值：\n',df1)
print('输出df1的和值：\n',sum(df1))
#组合条件筛选excel表
df_zh=df[df['PEP Element']=='ALL PRODUCT MDF']
print('PEP Element为ALL PRODUCT MDF''的和：',sum(df_zh['Revenue']))


df_zh1=df_zh[df_zh['Incentive ID']=='ACC00616495']
print('pep element&incentiveID的筛选和：',sum(df_zh1['Revenue']))
df_zh2=df_zh1[df_zh1['Payment Flag']=='Y']
print('根据pep element&incentiveID &payment flag筛选的结果：\n',sum(df_zh2['Revenue']))

#得到对应的列的值：
print('PEP Elementde的值：',df['PEP Element'])
pep=df.drop_duplicates(subset=['PEP Element'],keep='first')['PEP Element']
print('去掉PEP Elementde的重复值：\n',pep)
pep_vals=pep.tolist()
print('得到具体的pep element的值：\n',pep_vals)
pep.to_csv('pep.csv',encoding='utf-8')

#其他方式输出对应列的值(非常重要)
print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
zh=df.loc[:,['Incentive ID','PEP Element','Revenue']]
print(zh)
print(type(zh),type(df))
print(zh.loc[0:3])
zh.to_csv('zh.csv',encoding='utf-8')


'''
# #3、输出对应列的值
# # print('输出calculationID列的值：',df.loc[[:],['Calculation ID']])
#
# #按照值来刷选
# pf=(df['PEP Element']=='TOPSELLER') & (df['Incentive ID']=='454988')
# sd=df[pf]
# # print(type(sd))
# print('Payment Flag为Y的值：',sd)
# # sd.to_excel('pandas_excel.xlsx',encoding='utf-8')
# # print(sum(sd['Revenue']))'''