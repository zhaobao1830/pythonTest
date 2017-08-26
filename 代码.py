#! /usr/bin/env python
# -*- coding:utf-8 -*-

'''
author :ben
date : 2017-7-19
'''


# abs,max,min,sum,len,pow,range,sorted,divmod, round
# print(abs(-3 - 4j))
# print(max(1, 2, 3))
# print(max('e', 'd', 'a'))  # a-z
# print(max('22', '2', '21', '23', '199', 'a'))
# print(sum((1, 2, 3)))  # 内置的sun传入的参数是可迭代对象  iterable  for i in iterable
# print(len('python'))
# print(pow(2, 3, 2))  # 传入两个参数a,b  //c
# print(list(range(9)))
# print(sorted(['21', '2', '4', '33', '201'], reverse=True))  # sorted  # 从小到大排序
# print([1, 3, 2, 4].sort())  # 列表的方法 没有返回值
# print(divmod(8, 2))  # (商,余数)  # 打包tuple
# print(round(3.56)) # 5-9 进一位


# 类型转化  int，float,complex,long,str,ord,chr,unichr,bool,bin,oct,hex,list,slice,tuple,dict

# long 3.x已经不存在 int放到一起
# unichr  3.x已经不存在

# print(int('2'))
# print(float(-3))
# print(complex(2,3))  # 负   复数
# print(type(str(2)))
# print(list(range(6)))
# print(dict(name='haha',age=22))
# print(ord('abc'[1]))  # a--->97  ord   chr 97 --- 字符
# print(chr(97))

# print(bool(0))
# print(bool('   '))
# print(False + 3, True - 1)


# callable()  参数  判断传入参数对象是否可调用 # 方法    callable(可否调用)
# name = 'ben'
#
# def run():     # 函数/方法
#     # print('我正在跑步')
#     pass
# # print(callable('123'))
# # print(callable(max))
# #print(callable(name))  # 不能
# print(callable(run))   #

# slice函数   切片  注意第三个参数
# print((1, 2, 3, 4, 5)[slice(1, 3)])
# print((1, 2, 3, 4, 5)[1:3])
# print(list(range(20))[slice(1, 9, 2)])
# print(list(range(20))[1:9:2])


# 进制转换的内置函数
# 1,9十进制
# 八进制:0oxx
# 十六进制:0x15
# 二进制:0bxx

# 二进制转换 bin内置函数
# print(bin(20))
# print(oct(30))
# print(hex(10))

# all,any
# print(all((True, 1, {})))  # 内置all 所有的数据项都为True ---> True
# print(any([0, 1, '', {}]))  # 1- True  只要有一个数据项为T--->T

# sort/sorted    reversed 内置函数
# reversed 和排序有区别  位置颠倒了
# a_list = [5, 9, 6, 8]
# b_list = reversed(a_list)
# print(list(b_list))

# 类
class MyWork():  # self -->this 实例对象自身
    # name = 'tom'
    def make(self):
        print('正在制造汽车')

    def run(self):
        print('正在行驶')


# 类的外面
def go():
    print('汽车开始启动')


# 类的外部
name = 'ben'  #
# 创建一个类的实例对象
mclass = MyWork()  #
# 判断是否存在某个属性  hasattr (变量和函数)
# print(hasattr(mclass, 'name'))  # 参数
# 获取某个属性
# print(getattr(mclass, 'name', 1))  #第三个参数是获取不到的时候给的默认值
# 设置实例对象的某个属性值
setattr(mclass, 'run', '我开始启动')  # setattr没有返回值
# print(getattr(mclass, 'run'))  # 有

# 判断某个对象是否属于某个类型或者它的子类  object 基类
# print(isinstance(mclass, object))
# 第一个参数是否是第二个参数的子类
# print(issubclass(MyWork, object))


# str
# print(str('1+3'))

# repr 把传入的参数转换为python识别的字符串形式
# print(repr('1+3'))  # '1+3' 字符串
# print(repr(1 + 3))

# eval函数  计算字符串表达式的结果   计算结果的效果
# print(eval('1+3'))

# python交互环境的一个用法
# 自己去实践

# dir/help  # a_tuple-->tuple 属性列表
# a_tuple = (1, 2, 3)
# print(dir(a_tuple))
#
# print(a_tuple.__doc__)  # 文档字符串
# print(a_tuple.__class__)  #a_tuple-->类的类型
# print(a_tuple.__contains__(3))
# print(3 in a_tuple)
# help(a_tuple)   #查看帮助信息

# compile  编译  参数为字符串   print('gohome') 指令  exec 执行
# code = compile("print('gohome')", '', 'exec')
# print(type(code))
# eval(code)


#compile编译code(class) ,参数为字符串类型
#函数将一个字符串编译为字节代码
code = compile("open('mytext.py','w',encoding='utf-8').write('我是1706班')",'','exec')
print(type(code))
eval(code)
#读取文件里面的内容

#对文件操作open()
#json 模块 序列化和反序列化
