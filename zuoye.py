#! /usr/bin/env python
# -*- coding:utf-8 -*-

'''
author :ben
date : 2017-7-19
'''


#day02
#import
count = 6
while count > 0:     #  循环给6次机会
    try:
        grade = float(input('请输入你这次考试的得分:').strip())  #去掉字符串两端的空格 小数
        print(grade)
        if grade > 100 or grade < 0:  #  1000合适?  0-100  #or 或者   -10
            print('您输入的分数超出了范围!!')
        elif 90 <= grade <= 100:     #  grade > 90 and grade < 100
            print('您这次的成绩非常棒!再接再厉!')
        elif grade >= 80:
            print('你这次取得成绩等级为良好')
        elif grade >= 70:
            print('你这次取得的成绩等级为一般')
        elif grade >= 60:
            print('你这次取得的成绩有点差劲!')
        else:
            print('你这次的成绩等级为不合格!还要继续努力')
    except Exception as e:
        print('您输入的格式错误,请输入一个数值型')
    count -= 1
#1.input    是我们在控制台输入内容的内置()  返回值类型是字符串类型



#第三天的作业:  #''英文状态下    不要写中国输入法的''





# 1.完成函数文档字符串的使用

  # class MyWork():
  #     ''''
  #
  #
  #     '''
  # def  play_ball():
  #     '''
  #
  #     :return:
  #     '''
# 2.在你的command line中打印输出:
#     print('\\\n\\')看看会发生什么？
#     print(r'\\\n\\\')
#     print('\\\t\\')
#     print(r'\\\t\\')
# 3.name = 'tom'
#    age = 20
#    使用字符串格式化输出打印name和age



