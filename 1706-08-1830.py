def foo(x, y, z, *args, **kw):
    print('x =', x, 'y =', y, 'z =', z, 'args =', args, 'kw =', kw)
    # x = 1 y = 2 z = 3 args = () kw = {'name': 'jim', 'age': 28, 'add': '上海'}
    sum = x + y + z
    print(sum)
    # 6
    for i in args:
        print(i)
    # 没有值
    print(kw)
    # {'name': 'jim', 'age': 28, 'add': '上海'}
    for j in kw.items():
        print(j)
    # ('name', 'jim')
    # ('age', 28)
    # ('add', '上海')
a_tuple = (1,2,3)
# # 此处参数修改为2个看看会怎么样?
# # python里面的元组被定义后，是无法改变的
b_dict = {'name': 'jim', 'age': 28, 'add': '上海'}
foo(*a_tuple, **b_dict)
# 分析这里会怎么样?

# a_tuple里面的值会优先赋值给x,y,z
# 多余的值会赋值到args,所以现在args里面是空的
# b_dict里的值赋值给了kw

