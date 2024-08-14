import sys
import importlib



importlib.reload(sys)
import webbrowser
import time

import os
url="http://www.mayikt.vip/"
print("赤石工具箱v1.0版本")
while True:
    r=int(input("请输入你要使用的功能1:电脑电话,2.如何获取黄色小视频教程/如何免费观看于庆年2"))
    #if r==1:
        #print("欢迎使用开户工具")
        #name=input("请输入对方姓名")
        #xb=input("请输入对方性别(男/女/沃尔玛购物袋)")
        #gn=input("1.开对方的户2.开别人父母的户")
        #if gn==1:
        #    print("姓名:"+name+",性别"+xb)
        #if gn==2:
        #    print("父亲性别为男性，母亲性别为女性")
    if r==1:
        phone=input("请输入你要拨打的号码")
        print("请在手机上打开电话app输入以下文字:"+phone)
    if r==2:
        webbrowser.open(url)
