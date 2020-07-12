#coding:utf-8

import unittest
from ddt import data, ddt, unpack,file_data


json_python = {"CalcCode": "testcode", "Remarks": "test", "Submitter": "ligl6", "Approver": "duanmuqd1"}
@ddt
class test_se(unittest.TestCase):
    def setUp(self):
        pass
    @file_data(json_python)
    @unpack
    def test_01(self,**value):
        print(value.get('Remarks'))
    def tearDown(self):
        pass
if __name__ == "__main__":
    unittest.main()