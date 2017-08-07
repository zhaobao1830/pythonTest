a = input("请输入值:")
print('类型为：', type(a))
try:
    num = float(a)
    print(type(num))
    print('转换为数值型', num)
    if num <= 100:
        if num >= 90:
            print('你的成绩为优秀')
        elif num>=80 and num<90:
            print('你的成绩为良好')
        elif num>=60 and num<80:
            print('你的成绩为一般')
        else:
            print('你的成绩为不合格')
    else:
        print('输入的值不能大于100，请重新输入！')
except:
    print('请输入数字')