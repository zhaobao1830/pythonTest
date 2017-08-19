# 1.用while/for循环求计算1+3+5.....+45+47+49的值
i = 1
num = 0
while i < 50:
    num += i
    i +=2
print(num)

num = 0
for i in range(1, 50):
    if i%2 == 0:
        continue
    else:
        num += i
print(num)
# 2.代码实现斐波那契数列(比如前30个项)
def recur_fibo(n):
   """递归函数
   输出斐波那契数列"""
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))


# 获取用户输入
nterms = int(input("您要输出几项? "))

# 检查输入的数字是否正确
if nterms <= 0:
   print("输入正数")
else:
   print("斐波那契数列:")
   for i in range(nterms):
       print(recur_fibo(i))
