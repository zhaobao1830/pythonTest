#! /usr/bin/env python
#  coding:utf-8
# 具有特殊功能的注释代码
# ! /usr/bin/env python:  unix操作系统下边(linux)指明了解释器的路径
#  coding:utf-8 :指定当前这个脚本文件的编码格式为utf-8 ()

'''       #三引号
作者 :  陈哈哈      # 解释说明
时间 : 2017-8-7
出版信息:xxxx
公司:oooo

'''

# 字符串  一串串的字符    字符    'abc'---z  ABC_--Z  '100'  基本的认识

# 第一种字符串表现形式:单引号的字符串
# a = '1000000'
# print(a,type(a))

# 第二种字符串表现形式: 双引号  "   "
# b = "chenhaha"
# print(type(b))


# 为什么要分单引号和双引号

# print('my name is "ben"')   #
#
#
# print("hanbing  'ben' chenhah")

# 单引号内嵌套了双引号
# 双引号内嵌套了单引号

# print(type('ben'))
#
# print(type("阿曲"))

# print('我叫大笨蛋,我喜欢黄色')
# print('我的家庭住址在xxx')


# content = '''
# 我的名字叫陈哈哈!
# 我喜欢"lucy",
# 我喜欢打'篮球'~~~~~~~~~~
# '''
#
# #  '''     '''     /     """     """  都是可以的
# print(content)

# 设计三引号?
# 优势:
# 1.很多内容
# 2.保持原始的格式
# 3.三引号字符串内部可以嵌套单双引号


# 三引号作用;
# 1.定义字符串
# 2.解释说明
# 3.文档字符串


# 文档字符串-类
# class MyClass():
#     '''
#
#     '''
#
# print(MyClass.__doc__)   #  后面类型

# 文档字符换-函数
# def play():
#     '''
#     这是个玩游戏的一个方法
#     :return: None
#     '''
#
#     print('哥们,一起玩游戏!')
#
# print(play.__doc__)



# 字符串的连接     格式化的快捷  #
# print('tom   ', 'is    ', 'good    ', 'boy')   #print(1,2.3,'ben')   默认会一个格

# a = 'tom ' 'is ' 'good ' 'boy'
# print(a)


#  \n  换行
# b = 'tom ' + 'is ' + 'good ' + 'boy'  + 'and you'  # 可以+号连接字符串
# print(b)

#     \   字符串有续行  告诉解释器,这个字符串还没完,把后面串串给我加上去

# 续行符号前边是可以空格,后边是不能空格
# c = 'my name'\
#     'ben'
# print(c)


#  'it\'s dog!'   字符串的嵌套问题  # 单双引号的嵌套
# print('what\'s you name')   #转义字符\   '  后面这个单引号保持原样


# 嵌套

# 转义字符场景之一
# path = 'F:\\now'      #转义字符\   '  后面这个单引号保持原样
# print(path)


# text = 'i\'m study \n python'   #去掉了转义字符  (\n:特殊功能,换行)
# print(text)


# 原始字符串     r''(原始字符串)--- 所有具有转义特殊功能特殊字符---干掉特殊的功能
# text = r'i\'m study \n python'   #原始字符串简单来说去特殊化(\n,\t,\v,\b) (具有转义字符的一些特殊功能)
# print(text)
#
#
# c = r'ben'   (#原始字符)


# python注释
# 1.单号注释

# 注释的方式:
# 1.#    2.'''    '''

# print('陈哈哈')   #之后的代码是不会被解释执行


# print('1')      ctrl  +  /


# '''  '''

# print('1')
# print('1')
# print('1')
# print('1')
# print('1')
# print('1')
# print('1')


# 字符串格式化:第一种
# 作用
# print('my name is yaoming')

# %s  字符串的标记
# %s---字符串    %d---整数?    %f---浮点数    %s---能不能给数字?
# print('the price is %s, my name is %s ' % (11.11111, 'ben'))


# 字符串格式化:第二种:
# 字符串内部留空位{}--花括号
# content = '{} is boy, {} is {}'.format('ben', 'age', 18)  #前后要对应
# print(content)


# ord内置函数   字符---对应的整数  unicode
# print(ord('z'))
# print(ord('过'))

# chr内置函数   码表整数----字符   反向
# print(chr(2000))
# print(chr(888))


# 字符串长度  内置函数len使用  查看字符串的长度
# print(len('我不是小日本'))
# print(len('chenhaha'))


# 4个字节来表示     00000000  (1个字节)

# ASCII编码: 外国人常用的大小写英文字母、数字和一些符号, 一共127个字符,
# 用1个字节(byte)
# 可以涵盖完, 也就是8个位, 它将序列中的每个字节理解为一个字符
# Unicode编码: Unicode把所有语言都统一到一套编码里，避免乱码的出现
# Unicode用2 - 4
# 个字节(最少2个字节), 好, 乱码解决了, 可是看看英文字母吧?
# Unicode编码只是文字在内存中的内在形式


# ASCII编码:美国标准协会   a-z   A-Z  0-9  特殊字符  127   1个字节来表示,不能表示中文

# Unicode编码:最少用2个字节来表示     127   2个字节来表示   万国码(基本上全世界所有的字符集)

# 为了解决不其他人的字符集的使用,Unicode编码解决的问题

# Unicode编码解决的问题,又带来了一个新的问题:1个字节来表示127---->万国码(最少2个字节)
# 浪费了内存,浪费了资源


# utf-8编码:  Unicode编码,解决全世界通用的这个问题,一刀切(ASCII编码127,全用一个字节来表示),
# 超出范围之类可以用多个字节来表示,一举两得

# 1个字节    00001111




# python2.x  当前2.7
# a = '呵呵'   #  python2.x  str类型的字符串(默认的字符串类型)   # py2  str 1个中文3个字节来表示
# print len(a)   #len()  ---字节个数
#
# b = u'呵呵'   # unicode字符串     py2  u''   str(x)     unicode字符串  len   字符的个数
# print len(b)   #len()  ---字符的个数


# python3.6.2
# 默认的字符串类型全部为unicode字符串

#
# a = 'ben'
# print(a)


# 编码 encode()    #gbk编码(互联网)---你的项目(utf-8),可能会导致乱码问题  gbk--(解码)unicode--utf-8(编码)
# 解码 decode()

# encode(encoding): 将unicode转换为bytes，    编码
# decode(encoding)：将bytes转换为unicode，    解码


# python模块开发中,一般都有设置文件编码为utf-8, 在python3中已支持
#    Unicode编码,可以直接使用中文,python2中:u’我爱你’
#    ##如果没有特殊业务要求，请牢记仅使用UTF-8编码


# 普通字符串(unicode字符串)   字节类型字符串bytes()


# 字节类型字符串python3
# a = bytes([1, 2, 3, 4])
# print(a)
# print(type(a))
#
# b = b'ben'     # 特殊标记  b''
# print(type(b))
#
# c = '冰雪'   # str ---- 默认unicode字符串
# print(type(c))


# a = bytes('hello', 'ascii')
# print(type(a))
# print(a)


# a = 'hello world'

# b = '我爱大大'.encode('utf-8')     #encode(unicode---bytes(utf-8))
# print(b)    #   b'ben'     b'\xe6\x88\x91\xe7\x88\xb1\xe5\xa4\xa7\xe5\xa4\xa7'




# c = b'\xe6\x88\x91\xe7\x88\xb1\xe5\xa4\xa7\xe5\xa4\xa7'.decode('utf-8')    #解码    字节类型字符串---unicode(一默认编码)
# print(c)    #ben

#gbk编码      '我爱你'.decode('gbk').encode('utf-8')
#中间编码格式:unicode  ()


x = 'ben'.encode(encoding='gbk')
print(x)
y = x.decode()
# print(y)


# encode(encoding): 将unicode转换为bytes，    编码  (写入磁盘文件或者互联网上传输)
# decode(encoding)：将bytes转换为unicode，    解码


print('ben'.encode('utf-8'))    #b''字节类型字符串     'ben' (unicode编码字符串)
