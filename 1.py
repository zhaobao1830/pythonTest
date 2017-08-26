#! /usr/bin/env python
# -*- coding:utf-8 -*-

'''
author :ben
date : 2017-7-19
'''

# datetime模块: 对time重新包装,分2个维度,日期维度,时间维度
# import datetime  # 模块
# print(dir(datetime))
# print(datetime.__doc__)
# print(datetime.MAXYEAR)
# print(datetime.MINYEAR)
# print(datetime.__name__)


# datetime模块里面的datetime类
# from datetime import datetime   # 类
# #print(dir(datetime))
# print(datetime.max,datetime.min)   #年月日小时分秒
# print(datetime.resolution)  #最小维度单位从小时开始

# datetime类里面定义的函数
# from datetime import datetime, time, date
#
# time_a = time(21, 55, 44)  # time类的实例对象
# date_b = date(2017, 8, 25)   # date实例对象
#
# datetime1 = datetime(2017, 8, 25,8, 55, 44)
# datetime2 = datetime.now()   # 当前日期时间  # 重点函数
# print(datetime.today())   #
# print(datetime2)


# now  utcnow函数   日期信息,小时上间隔8个小时
# print(datetime.utcnow())  # 格林威治表示时间

# print(datetime.combine(date_b,time_a))   # 组合 (日期+时间)

# 如何把datetime对象转化为指定格式字符换表现形式

# date_str= datetime.strftime(datetime2,'%Y/%m/%d %H/%M/%S') # datetime对象
# print(type(date_str))
# print(date_str)
#
# print(datetime2.date().strftime('%Y/%m/%d'))
# print(datetime2.time().strftime('%H/%M/%S'))



# datetime类一些函数
# from datetime import datetime
#
# datetime1 = datetime.now()
# print(datetime1.timetuple())  # tuple
#
# datetime2 = datetime1.replace(2022, 8, 8, 21, 15, 55,99999)  #replace替换
# print(datetime2)
#
# # 重要函数  now函数,strftime,replace
# print(datetime1.weekday())   # 星期五-1
# print(datetime1.isoweekday())  # 星期几对用
#
# print(datetime2.isoformat())  # 返回格式 2017-08-25
#
# print(datetime2.isocalendar())  # (2017,08,25)  #

# 几种格式的转换

# 1.datetime对象转换为时间搓
import datetime
from datetime import datetime  # 类
# datetime1 = datetime.now()
# time_stamp = datetime1.timestamp()
# print(type(time_stamp))   # 小数表示的时间搓
# print(time_stamp)  # 是以某个特定的时间节点为开始

# 2.时间搓--->datetime对象   # utc-时间间隔了8个小时
# time_stamp = 88888
# datetime1 = datetime.fromtimestamp(time_stamp)
# datetime2 = datetime.utcfromtimestamp(time_stamp)
# print(datetime1)
# print(datetime2)


# 3.第三种转化  (两个方面的转化)
# datetime转化为字符串            strftime
# 时间str--> datetime对象        strptime
# date_str = datetime.strptime('2017/8/25 21:49:33','%Y/%m/%d %H:%M:%S')
# print(type(date_str))


# 在原因的日期时间上增加指定指定的时间
# from datetime import datetime, timedelta  # 类
#
# datetime1 = datetime.now()
# datetime2 = datetime1 + timedelta(days=2, hours=6)
# print(datetime2.strftime('%Y/%m/%d %H:%M:%S'))
#
# datetime3 = datetime1 - timedelta(days=10,hours=3,minutes=30)
# print(datetime3.strftime('%Y/%m/%d %H:%M:%S'))


# now函数,strftime,strptime,replace,timedelta(时间推移),第三种转化




# os 主要是和操作系统相关的属性
import os  # 内置模块

# print(os.name)   # 操作系统系列  微软操作系统---> windows nt(win7)
# print(os.stat('home.py'))  #参数文件所对应的一些属性信息
# print(os.getcwd())  # 当前这个脚本文件所在的全目录路径
# print(os.getenv('python','没有这个系统变量'))  #获取系统环境变值
# os.environ['age'] = 'tom'  # 设置系统变量

# 两种方式去获取系统环境变量值getenv  / environ['']如果不存在会报错
# print(os.getenv('name','0'))  # 获取系统变量
# print(os.environ['name'])  #

# 获取目录信息的方法
# print(os.listdir(r'F:\project\other\vip_python\day11'))
# print(os.listdir('.'))  # 默认当前脚本所在的目录



# 创建一个目录 mkdir 注意一点:如果当前这个文件夹已经存在,会报错
# os.mkdir('home')

# 创建多级目录
# os.makedirs('./home/wowo')

# 重新命名文件名
# os.rename('home.py', 'ben.py')
#os.renames('ben.py','tom.txt') # 可以多层次修改


#删除文件夹rmdir
#os.rmdir('./home')

#os模块里面一个执行脚本代码的方法,参数是你要执行的指令
#os.system('ping www.baidu.com')
#os.system("print('i am is ben')")
#os.system('dir')  # 目录清单




#os.path 模块
# from os import path
# # print(path.split('./ben.py'))  # (目录信息,文件信息)  split切割
# # print(path.isfile('.'))  # day11是目录
# # print(path.isdir('.'))  #
# # print(path.exists('./ben.py'))  # 是否存在
# # print(path.getsize('./ben.py'))  # 获取文件内容的大小,字节单位
#
# print(path.join('.','/ben.py'))  # 目录和文件的拼接
#
# print(path.basename('ben.py'))
#
# print(path.dirname('./ben.py'))  # 获取文件目录信息

#json模块 把python数据类型-->json数据格式:1.内存中数据写入到本地磁盘,
# 2.把python数据类型转换为json统一的格式在互联网上传播

#python数据类型:None,bool,int,float,string,list,tuple,dict

import json

# a_list =[1,2,3]
# a_str = json.dumps(a_list)  # python数据类型-->json
# # print(a_str)    # json
# # print(type(a_str))
#
# # dump直接序列化/dump需要文件
#
# with open('json.txt','w') as f:  #创建一个文件名  dump
#     json.dump(a_list,f)
#
# b_list = json.loads(a_str)  # 反序列化回来
# print(b_list)
# print(type(b_list))

#loads直接反序列化,load也是文件操作相关
# with open('json.txt','r') as file:
#     content = json.load(file)  # 反序列化 json--->python数据类型
#     print(type(content))
#     print(content)











