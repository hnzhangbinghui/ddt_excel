import re
import pandas as pd
import numpy as np
df=pd.read_excel(r'C:\Users\LX\Desktop\summary and  details\test_data.xlsx')
print('整个excel表的Dataframe：\n',df)
'''
loc:从索引中获取具有特定标签的行或者列
iloc：在索引中的  特定位置  获取行或者列，因此只接受整数；
ix：通过行标签或行号索引数据，是loc and iloc的混合
'''
print('loc行:\n',df.loc[0])
print('没有索引时的列值：\n',df['Calculation ID'])
print('iloc行:\n',df.iloc[0])

'''第一部分：使用ix切分series'''
# s=pd.Series(np.nan,index=[49,48,47,46,45, 1, 2, 3, 4, 5])
# print(s)
# print('读取前三行，因为iloc把3看成是位置position：\n',s.iloc[:3])
# print('此条代码却读取的是前八行的数据，因为loc把3看作是索引的标签了：\n',s.loc[:3])
'''第二部分，在Dataframe中使用ix实现复杂切片
ix函数（0.20.0版本后已经弃用）
ix就是一种混合索引，字符串的标签和证书的数据索引都可以作为合法输入，其实相当于loc和iloc的一个混合方法：
test_dict_df.ix['Alice']
test_dict_df.ix[1]
'''
#loc,可以是单个标签，可以是多个标签，也可以是切片array，还可以是行标签，列标签，还可以是行标签和列标签都是切片,
#还可以接受条件进行筛选
print('输出1,2,5行：\n',df.loc[[1,2,5]])   #两个中括号
print('切片输出：\n',df.loc[1:10])
print('输出其中的也cell值：\n',df.loc[1,'Calculation ID'])    #一个中括号
print('行标签和列表区都是切片:\n',df.loc[1:4,'Calculation ID':'Revenue'])

print('loc接受条件筛选：\n',df.loc[df['Revenue']>10000])
'''当然，也可以再条件选择后，再加入列选择，列选择的时候可以单列，也可以是切片数组，通过上面的介绍这里就可以灵活处理：
test_dict_df.loc[test_dict_df['english']>90,'english'] #single label
test_dict_df.loc[test_dict_df['english']>90,'english':'name'] #slice array
test_dict_df.loc[test_dict_df['english']>90,['english','name']] #label array'''

#iloc,也接受切片
#at函数，是用来选择单个值的，用法类似于loc
print('at:\n',df.at[1,'Revenue'])
print(df.loc[1,'Revenue'])
#以上两种方法都能选择到，label为1，列为'english'的那个值，但是据说at速度要快，
#、iat函数
# iat函数相对于at函数，就相当于iloc相对于loc函数。iat也只能选择一个值。只不过是用索引位置来选择，注意：行列都是索引位置来选择，从0开始数。
# # test_dict_df.iat[1,'english'] #error!!!
# test_dict_df.iat[2,2] #right!!!
print(df.iat[1,1])




