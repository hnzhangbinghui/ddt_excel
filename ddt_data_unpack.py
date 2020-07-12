#coding:utf-8

import unittest
from ddt import data, ddt, unpack

@ddt
class test_se(unittest.TestCase):
    def setUp(self):
        pass
    @data((1,2),(3,4),(5,6))   #对于两个参数
    @unpack
    def test_01(self, value1,value2):
        print(value1,value2)
    def tearDown(self):
        pass
if __name__ == "__main__":
    unittest.main()