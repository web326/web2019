import  testloadtest
import unittest
import HTMLTestRunner,os
def createsuit():
    '''创建测试方法'''
    test_unit= unittest.TestSuite()
    test_dir = r"脚本保存路径"
    testlist = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py", top_level_dir=None)
    for test_suit in testlist:
        for testcase in test_suit:
            test_unit.addTest(testcase)
    return  test_unit

with open("result.html","wb") as file:
    '''生成测试报告'''
    runner = HTMLTestRunner.HTMLTestRunner(stream=file,title="测试报告",description="执行用例")
    runner.run(createsuit())

