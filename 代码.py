#! /usr/bin/env python
# -*- coding:utf-8 -*-

'''
author :ben
date : 2017-7-19
'''

# list(列表)  # python里面的可以容纳很多对象的一个容器

# name_list = []
# age_list = list((1,2,3))  #
# print(type(name_list))
# print(len(name_list))
# print(age_list)


#  求列表长度  (len)

#  列表的索引   也是从0开始    #支持负索引   #索引越界的问题
# name_list = ['tom', 'ben', 'cici', 1, 2, 3, 4, 5, 6, 7, 8, 9]  # 9对应的索引
# print(name_list[-1])

# 列表操作(增,删,修改)
# 很重要的特性就是定义好之后是可变的

# 末尾追加元素
# num_list = [34, 56, 88]
# num_list.append(99)  #追加位置末尾
# num_list.append('ben')
# print(num_list)


# 在指定的位置添加元素

# num_list = [34, 56, 88]   #不包含
# num_list.insert(-1,'haha')     #插入元素  第一个参数为索引,第二个参数是插入的元素
# print(num_list)

# 弹出元素
# num_list = [34, 56, 88]
# #pop没有参数,弹出的是最后一个元素
# num_list.pop()
# print(num_list)


# 有参数的情况下:pop
# num_list = [34, 56, 88]
# num_list.pop(0)
# print(num_list)


# 删除元素  remove  参数一定要注意列表里面的元素
# num_list = [34, 56, 88]
# num_list.remove(88)
# print(num_list)


# 修改元素
# num_list = [34, 56, 88]
# num_list[0] = 'ben'
# print(num_list)
# num_list[-1] = True
# print(num_list)
# num_list[3] = 'haha'
# print(num_list)

# list嵌套

# str_list = ['ben', 'chenhaha', 'aqu']
# num_list = [1, 2, 3, 4, 5, str_list]
# print(num_list[5][1])



# tuple 和列表  定义tuple
# name_tuple = ('ben','bingxue')
# print(type(name_tuple))
# print(len(name_tuple))

# 取tuple里面的元素
# name_tuple = ('ben', 'bingxue', 1, 2, 4)
# print(name_tuple[-1])


# tuple的一个陷阱
# age_tuple = ('ben',)    #  tuple ----  int
# print(type(age_tuple))

# tuple里面一个元素的时候,一定要注意写法,强制的规定

# tuple数据类型特征(),不是所有的()都是tuple,逗号

# tuple和list的一个重要的区别所在:
# list显著特征就是可改变性


# tuple的不可改变性
# age_tuple = (22, 21, 19, 34,'ben')   #逗号才是关键,而不是()
# age_tuple[0] = 'ben'
# print(age_tuple)

# age_tuple.append('ok')   # 不支持改变
# print(age_tuple)

# name_tuple = ()  #  0个元素1个元素要注意一下
# print(type(name_tuple))
# print(len(name_tuple))

# tuple可嵌套   不可改变的
# age_list = (33, 55)
# age_tuple = (18, 22, 34, age_list)
# #取嵌套元素
# print(age_tuple[3][1])
#
# age_tuple[3][0] = 'ben'
# print(age_tuple)




# num_list = [1, 2, 3, 4, 5, 6, 7, 8]
# a_list = num_list[:7:2]
# print(a_list)

# tuple的不可改变性,为什么又支持切片?
# num_tuple = (1, 2, 3, 4, 8, 10, 11, 12, 13, 14, 15, 16)  # 告诉了我们tuple也是支持切片操作
# a_tuple = num_tuple[1:4:-1]  # 不包含右边的索引(不要8)
# 如果切片第一个参数为空,要分两种情况:
# 1.看第三个参数:正数  结合起来,从左往右切,开头为0索引


# 如果切片第一个参数为空,要分两种情况:
# 1.看第三个参数:负数   结合起来,从右边到左边(负数)   默认从右边的第一个元素切
# print(a_tuple)
# print(num_tuple)


# 问题:   list[0.........100]
#   tuple(0.........100)


# list和tuple区别:
# 相同点:
# 1.都是python里面序列之一.   (容器,每一个元素都是有编号的,比如索引)   索引
# 2.list和tuple里面每一个元素都是有顺序的,索引,index属性
# 3.list和tuple都是可循环迭代的   (单书架,每一本书都有对应的编号)
# 4.list和tuple里面元素自身的类型可以不一样
# 5.list和tuple都是支持负索引(方便我们去操作右边的元素)
# 6.list和tuple都支持python切片操作
# 7.list和tuple都可以获取里面的元素 (索引)


# 不同点:
# list定义好之后是可以去修改,tuple定义好之后是不可以去修改元素  # 最大的区别


# 问题:
# python里面既然有了万能list,为什么要设计tuple数据类型?
# num_list = [1,2,3]
# num_tuple = (1,2,3)  #不ok,不能添加4  功能有缺失的感觉

# 设计tuple数据类型的目的:
# 1.安全稳定
# 2.对于容器里面的元素来了限定(指定死了只能放这些)

# 抽屉:只能放3样东西:  剪刀,石头,布  tuple


# list和tuple都是序列之一:可循环迭代
# name_list = ['tom', 'ben', 'lucy']
# for name in name_list:    #for循环  结尾:
#     print(name)
#     # if name == 'ben':
#     #     print('找到了ben老师')
#
# age_tuple = (10,12,13)
# for age in age_tuple:
#     print(age)


# 元素自身添加索引内置函数  enumerate (取元素的同时添加一个索引)
# a_list = [1, 3.14, 'haha', 99]
# for index, item in enumerate(a_list):
#     print(index, item)


# 排序list
#sort方法是list的方法,没有返回值的,只是对原来的list进行排序

# a_list = [2, 5, 1, 10, 16]
# # print(a_list.sort(reverse=False))   #sort  排序    #reverse是否反转
# # print(a_list)
#
# #区别之一:
# # sorted 有返回值
# # sort是list的方法,sorted是python内置的方法
#
# b_list = sorted(a_list,reverse=True)  #返回值赋值给了b_list
# print(b_list)



#python写代码简单
# x,y = 1,2
# x,y = y,x   # a = temp  temp= b  b = a  java,安卓
# print(x,y)

def func(a, b, c, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


# func(1, 2)
# func(1, 2, 3)
# func(1, 2, 3, 4)
# func(1, 2, 3, 4, 5)
# func(1, 2, 3, 4, 5, 6, name='jim')
a_tuple = (1,2)
func(*a_tuple, name='tom', age=22)