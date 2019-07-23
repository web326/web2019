import unittest
import  requests
import HTMLTestRunner
import  time,os
class NationLand(unittest.TestCase):
    '''这是用地批次管理接口测试'''

    def setUp(self):
        self.url = "http://192.168.0.197:8088/land/showList"

    def testshowList(self):
        '''current 默认为1，代码页码,size 默认为 10'''
        # self.url = "http://192.168.0.197:8088/land/showList"
        form ={
          "CODE": "",
          "LANDBATCH": "",
          "current": "2",
          "size": "10"
        }
        r = requests.post(self.url,data=form)
        code = r.status_code
        self.assertEqual(200,code)
        print("测试通过")

    def testcurrenIsnull(self):
        '''current 为空,size为正常10'''
        form = {
            "CODE": "",
            "LANDBATCH": "",
            "current": "",
            "size": "10"
        }
        r = requests.post(self.url, data=form)
        code = r.status_code
        self.assertEqual(400,code)
        print("测试通过")

    def testsizeIsnull(self):
        '''current 为空,seze为正常10'''
        form = {
            "CODE": "",
            "LANDBATCH": "",
            "current": "1",
            "size": ""
        }
        r = requests.post(self.url, data=form)
        code = r.status_code
        self.assertEqual(400, code)
        print("测试通过")

    def testcursizeIsnull(self):
        '''current 为null,seze为null'''
        form = {
            "CODE": "",
            "LANDBATCH": "",
            "current": "",
            "size": ""
        }
        r = requests.post(self.url, data=form)
        code = r.status_code
        self.assertEqual(400, code)
        print("测试通过")


    def tearDown(self):
        pass

