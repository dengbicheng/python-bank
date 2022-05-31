#本程序用于连接湖南水利水电网络登录界面

import requests
import time

#网页登录
ulr = "http://10.251.224.2/drcom/login?callback=dr1650714108465&DDDDD=202140210015&upass=Dengbicheng0810.&0MKKey=123456&R1=0&R3=0&R6=0&para=00&v6ip=&_=1650714099933"

data = {
    "callback": "dr1650714108465",
    "DDDDD": "",   #这里输入你的网络账号
    "upass": "",   #网络密码
    "0MKKey": "123456",
    "R1": "0",
    "R2":"",
    "R3": "1",
    "R6": "0",
    "para": "00",
}

header = {
    "Accept": "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Connection": "keep-alive",
    "dnt": "1",
    "Host": "10.251.224.2",
    "Referer": "http://10.251.224.2/a79.htm",
    "sec-gpc": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50",
    "X-Requested-With": "XMLHttpRequest"
}
#当程序运行时
if __name__ == '__main__':
    print("正在连接请稍等...")
    #延迟5秒
    time.sleep(5) #这里延迟可以删除主要是为了仪式感
    #登录网页
    response = requests.post(url=ulr, data=data, headers=header)
    print("连接成功")











