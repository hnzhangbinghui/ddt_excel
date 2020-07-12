#coding:utf-8
import yaml
file=open('cofig.yaml')
#将yaml文档转换为python的字典
yml=yaml.load(stream=file,Loader=yaml.FullLoader)
print(yml)
print(type(yml))

#将python对象转换为yaml文件
py={'name': 'jack', 'age': 1110, 'children': {'name': 'jason', 'age': 2222, 'name_1': 'jeff', 'age_1': 3333},
    'children1': {'name': 'jason', 'age': 2222, 'name_1': 'jeff', 'age_1': 3333}}
yaml_test=yaml.dump(py)
# #写json文本
# f=open('test.yaml','w')
# yaml.dump(yaml_test,f)

#YAML格式除了可以转换为字典格式，还可以转换为列表或者符合结构的数据（比如字典数据类型和列表的混合数据类型）





