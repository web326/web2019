import functions
import time
import os
import pustil

########
# 获取开机以来 接收/发送 的字节数
# 依赖: psutil 库
# 参数(sent): Ture--返回发送的字节数 , False--不返回
# 参数(recv): Ture--返回接收的字节数 , False--不返回
# 两个参数都为(True): 返回包含 接收/发送 字节数的列表
# 函数失败返回: None
def io_get_bytes(sent=False,recv=False):
    internet = psutil.net_io_counters()  # 获取与网络IO相关的信息
    if internet == None:                 # 如果获取IO信息失败
        return None
    io_sent = internet.bytes_sent        # 开机以来发送的所有字节数
    io_recv = internet.bytes_recv        # 开机以来接收的所有字节数
    if sent == True and recv == True :
        return [io_sent,io_recv]
    elif sent == True:
        return io_sent
    elif recv == True:
        return io_recv
    else:
        return None                      # 参数不正确, 返回None

interval = 1                        # 每隔 interval 秒获取一次网络IO信息, 数值越小, 测得的网速越准确
k = 1024                            # 一 K 所包含的字节数
m = 1048576                         # 一 M 所包含的字节数
while True:
    byteSent1 = functions.io_get_bytes(sent=True)  # 获取开机以来上传的字节数
    byteRecv1 = functions.io_get_bytes(recv=True)  # 获取开机以来下载的字节数
    time.sleep(interval)                           # 间隔 interval 秒
    os.system('cls')                               # 执行清屏命令
    byteSent2 = functions.io_get_bytes(sent=True)  # 再次获取开机以来上传的字节数
    byteRecv2 = functions.io_get_bytes(recv=True)  # 再次获取开机以来下载的字节数
    sent = byteSent2-byteSent1                     # interval 秒内所获取的上传字节数
    recv = byteRecv2-byteRecv1                     # interval 秒内所获取的下载字节数
    unit = 'B/'+str(interval)+'秒'                 # 显示的速度单位, 每次显示前重置单位为( 字节(B)/秒(S) )
    if sent > m or recv > m :             # 字节数达到 m 级别时以 M 作为单位
        sent = sent / m
        recv = recv / m
        unit = 'M/'+str(interval)+'秒'
    if sent > k or recv > k:              # 字节数达到 k 级别时以 K 作为单位
        sent = sent / k
        recv = recv / k
        unit = 'K/'+str(interval)+'秒'
    print('上传速度: %5d %s' %(int(sent),unit))
    print('下载速度: %5d %s' %(int(recv),unit))
