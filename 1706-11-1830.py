# 1.datetime,获取你当前系统时间三天前的时间戳;并把当前时间戳增加
#  899999,然后转换为日期时间对象,把日期时间并按照%Y-%m-%d %H:%M:%S
#  输入打印这个日期对象,并获取date属性和time属性,最后判断当前日期时间
#  对象是星期几;
from datetime import datetime,timedelta
import time

# 系统时间三天前的时间戳
threeDay = datetime.now() - timedelta(days=3)
# print(threeDay)
threeTimetuple = threeDay.timetuple()
threeTimeStamp = int(time.mktime(threeTimetuple))
# print(threeTimeStamp)
newTmieStamp = threeTimeStamp + 899999
print(newTmieStamp)
# 增加899999以后的新时间
newTime = datetime.fromtimestamp(newTmieStamp)
print(type(newTime))
# # date属性和time属性
print(newTime.date())
print(newTime.time())
# 当前日期时间对象是星期几
print(newTime.isoweekday())


# 2.使用os模块线获取当前工作目录的路径,并打印当前目录下所有目录和文件,
#  获取当前脚本的绝对路径,获取当前脚本文件的绝对路径,分割当前脚本
#  文件的目录和文件在tuple中并判断当前文件所在的目录下存不存在文件
#  game.py,如果不存在则创建该文件.并往该文件里写入数据信息,然后
#  判断当前目录下是否存在目录/wow/temp/,如果不存在则创建,最后把目录
#  名称改为:/wow/map/

import os
from os import path
lujin = os.getcwd()
print(lujin) #当前工作目录的路径
mulu = os.listdir(lujin)
print(mulu) #打印当前目录下所有目录和文件
print(os.path.abspath(lujin)) #获取当前脚本的绝对路径
mulu_tuple = tuple(mulu)
print(mulu_tuple)
if ('game.py') in mulu_tuple:
    pass
else:
    zbfile = compile("open('game.py','w+',encoding='utf-8').write('zhaobao')", '', 'eval')
    eval(zbfile)
    rzbfile = open('game.py', 'r+', encoding='utf-8').read()
    eval("print('输出game.py内容:',rzbfile)")
print(path.exists('/wow/temp/'))
if path.exists('/wow/temp/'):
    os.rename("/wow/temp/", "/wow/temp/")
else:
    os.makedirs('/wow/temp/')

# 3.使用json模块完成序列化和反序列化
import json
a_list =[1,2,3]
a_str = json.dumps(a_list)
print(a_str)
b_list = json.loads(a_str)
print(b_list)
print(type(b_list))