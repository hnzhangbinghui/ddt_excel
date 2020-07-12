# coding:utf-8
'''
ddt中的data，unpack，file_data实现数据驱动，数据分离
1、@file_data，可以获取json文件和yaml文件的数据；
   需要把数据放入独立的json文件中，使用file_data，应用json文件中的内容，与def函数中的参数个数对应

'''
import unittest
from ddt import data, ddt, unpack


# json_python = {"CalcCode": "testcode", "Remarks": "test", "Submitter": "ligl6", "Approver": "duanmuqd1"}
@ddt
class test_se(unittest.TestCase):
    def setUp(self):
        pass
    @data(1,2,3,4,5,6,7,8,9)
    def test_01(self, value):
        self.assertEqual(value,5)
        #print(value)
    def tearDown(self):
        pass
if __name__ == "__main__":
    unittest.main(verbosity=5)
