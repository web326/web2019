import requests
import threading
#设置线程数
THEEND_NUM = 1
#设置线程需要执行数量
ONE_WORKER_NUM=1
#需要测试的并发用例
def gest():
    pass
#定义函数来循环执行测试用例
def work():
    global ONE_WORKER_NUM
    for num in range(1,ONE_WORKER_NUM):
        gest()
#添加线程，启动线程，
def thread():
    global  THEEND_NUM

    threads=[]
    for th in range(0,THEEND_NUM):
        t = threading.Thread(target=work ,name='t' + str(th))
        #设置守护线程
        t.setDaemon(True)
        threads.append(t)
    #循环开启线程
    for t in threads:
        t.start()
    #
    for t in threads:
        t.join()

if __name__ == '__main__':
    thread()
