num_list = [[1,2],['tom','jim'],(3,4),['ben']]
# 1. 在’ben’后面添加’kity’
num_list.append('kity')
print(num_list)
# 2. 获取包含’ben’的list的元素
for item in num_list:
    if 'ben' in item:
        print(item)
# 3. 把’jim’修改为’lucy’
num_list[1][1] = 'lucy'
print(num_list)
# 4. 尝试修改3为5,看看
for index, item in enumerate(num_list):
    if type(item) == tuple:
        break
    elif type(item) == list:
        if (3 in item):
            i = item.index(2)
            item[i] = 5
    elif type(item) == str:
        break
    elif type(item) == int:
        item = 5
print(num_list)
# 5. 把[6,7]添加到[‘tom’,’jim’]中作为第三个元素
num_list[1].append([6,7])
print(num_list)
# 6.把num_list切片操作:
#      num_list[-1::-1]
num_list[-1::-1]
print(num_list)