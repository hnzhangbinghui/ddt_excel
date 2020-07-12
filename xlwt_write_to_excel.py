import requests
from bs4 import BeautifulSoup
import pandas as pd

file=requests.get('https://www.dytt8.net/').content.decode('gbk','ignore').encode('utf-8')
bs=BeautifulSoup(file,'html.parser') #设置缩进格式，显示代码

dict_movie={}
for item in bs.select('a',limit=5):
    dict_movie[item.text]=item['href']
del dict_movie['']
print(dict_movie)
list_movie=[]
list_movie.append(dict_movie)
list_movie.append(dict_movie)
list_movie.append(dict_movie)
list_movie.append(dict_movie)
print('字典列表',list_movie)
pd.DataFrame(list_movie).to_excel('to_excel.xlsx',index=False,encoding='utf-8')

def export_excel(export):
    #将字典列表转化为DataFrame
    pf=pd.DataFrame(list_movie,columns=['最新影片','欧美电影','经典电影','国内电影'])
    #指定字段顺序
    order=['最新影片','欧美电影','经典电影','国内电影']
    pf=pf[order]
    #列名替换为中文
    columns_map={'最新影片':'A','欧美电影':'B','经典电影':'C','国内电影':'D'}
    pf.rename(columns=columns_map,inplace=True)
    file_path=pd.ExcelWriter('xlwt_write_to_excel.xlsx')  #指定生成的excel表格名称
    #替换空单元格
    pf.fillna(' ',inplace=True)
    #输出
    pf.to_excel(file_path,encoding='utf-8',index=False)
    file_path.save()
if __name__=='__main__':
    export_excel(list_movie)


#参考：https://www.cnblogs.com/zhengxt-520/p/11446121.html




