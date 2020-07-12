#coding:utf-8

'''
JSON是清零及的数据交换格式，json特点是：可读性强，有利于机器的解析和生成，一般用于提升网络的传输速率；
python处理json这种格式的数据库，需要先导入JSON类库 import json
有两个比较重要的方法：dumps（），将python对象编码成JSON字符串
loads，将JSON字符串编码成python对象
'''
import json
py_data={ "CalcCode":"testcode","Remarks":"test","Submitter":"ligl6","Approver":"duanmuqd1" }
json_python=json.dumps(py_data)
print("python：",py_data,type(py_data))
print("JSON:",json_python,type(json_python))

py_data2=json.loads(json_python)
print("JSON TO PYTHON:",py_data2)

# #写json文本
# f=open('test.json','w')
# json.dump(json_python,f)

#读取json字符串
fp=open('test.json','r')
dict=json.load(fp)
for k ,v in dict.items():
    print(k,v)

