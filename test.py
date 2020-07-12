#coding:utf-8
from ddt import ddt,file_data,data,unpack
from dataexcel import get_data
import unittest
from selenium import webdriver
import time
import HTMLTestRunner
import xlrd,xlwt

excel=get_data('',1)
@ddt
class test_se(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.get('https://login.hand-china.com/sso/login?')
        self.driver.implicitly_wait(20)

    @data(*excel)
    def test_01(self,dic):
        self.driver.find_element_by_id('username').send_keys(dic.get('username'))
        self.driver.find_element_by_id('password').send_keys(dic.get('passwd'))
        print(dic)
        self.assertEqual(dic.get('username'),dic.get('passwd'))
        print('111')
    def tearDown(self):
        self.driver.quit()
if __name__=='__main__':
    unittest.main()
    suite=unittest.TestSuite()
    suite.addTest(test_se("test_01"))
    file_path = "E:\\1124.html"
    fp = open(file_path, "wb")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp, title='DDT+Excel批量用户登录测试', description='四次登录，两次失败，两次正确')
    runner.run(suite)
    fp.close()



