import unittest
import os
from time import strftime

from demo.TestSet.testAdd import TestAdd
from demo.TestSet.testSub import TestSub
from demo.TestSet.extensions import fixtures

if __name__ == '__main__':
    "方法一：main方法使用TestLoader类来搜索，目前引入模块中所有以test命名开头的测试方法，"
    "并自动执行它们。"
    unittest.main()

    "方法二：构建测试套件来运行测试用例"
    # 使用addTest方法构造测试集(Test Suite)
    suite = unittest.TestSuite()
    suite.addTest(TestAdd('test_add1'))  # addTest(类('方法名'))
    suite.addTest(TestAdd('test_add2'))
    suite.addTest(TestSub('test_sub1'))
    suite.addTest(TestSub('test_sub2'))

    # 运行测试集合(Test Runner)
    runner = unittest.TextTestRunner()
    runner.run(suite)

    "方法三：通过defaultTestLoader类的discover()方法，自动查找指定目录下所有匹配模块的测试用例。"
    "使用TextTestRunner执行用例，生成Text报告。"

    # discover方法可以递归查找到子目录下的测试模块，前提是子目录下需要有一个__init__.py命名的空文件。
    discover = unittest.defaultTestLoader.discover('./demo/TestSet', pattern='test*.py')

    # 使用文本方式执行
    runner1 = unittest.TextTestRunner()
    runner1.run(discover)

    "方法四：使用 discover()方法查找指定目录下匹配的测试用例，使用HTMLTestRunner执行用例，"
    "生成HTML报告。"
    # 使用HTML方式执行
    from HTMLTestRunner import HTMLTestRunner

    now = strftime('%Y-%m-%d %H_%M_%S')
    result = open('./demo/log/' + now + ' result.html', 'wb')

    discover = unittest.defaultTestLoader.discover('./demo/TestSet', pattern='test*.py')
    runner2 = HTMLTestRunner(
        stream=result,
        title='测试报告',
        description='用例执行情况：')

    runner2.run(discover)
    result.close()
