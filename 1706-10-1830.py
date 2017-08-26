# 1.a_list = [1, 2, 3, 2, 2]
# 删除a_list中所有的2
a_list = [1, 2, 3, 2, 2]
while True:
    if 2 in a_list:
        a_list.remove(2)
    else:
        break
# 2.用内置函数compile以字符串的形式创建一个文件xx.py,在文件里写你的名字,然后用
# eval函数读取文件中内容,并打印输出到控制台
zbfile = compile("open('zb.py','w+',encoding='utf-8').write('zhaobao')", '', 'eval')
eval(zbfile)
rzbfile = open('zb.py', 'r+', encoding='utf-8').read()
eval("print('输出zb.py内容:',rzbfile)")

# 3.写一个猜数字的游戏, 给5次机会, 每次随机生成一个整数, 然后由控制台输入一个
# 数字, 比较大小.大了提示猜大了, 小了提示猜小了.猜对了提示恭喜你, 猜对了.
# 退出程序, 如果猜错了, 一共给5次机会, 5
# 次机会用完程序退出.
n = 5
import random
while n > 0:
    randNum = random.randint(0,100)
    print(randNum)
    myNum = int(input('请输入0到100之间的数字：'))
    if myNum < randNum:
        print('猜小了')
    elif myNum == randNum:
        print('猜对了')
        break
    else:
        print('猜大了')
    n -= 1