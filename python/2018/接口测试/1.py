import unittest
import  requests
import  time
class NationLand(unittest.TestCase):
    '''换成你公司的项目介绍'''

    def setUp(self):
        self.url = "换成你公司的接口地址"

    def testshowList(self):
        '''current 默认为1，代码页码,size 默认为 10'''
        land.setUp()
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
        land.setUp()
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
        land.setUp()
        '''current 为null,seze为null'''
        land.setUp()
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


if __name__ == '__main__':

    test_dir = r"脚本保存路径"
    testlist = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py", top_level_dir=None)

    runndr = unittest.TextTestRunner()
    runndr.run(testlist)

