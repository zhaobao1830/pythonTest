# 1.自己写一个字典,添加,删除,更新,清空操作
dict1 = {'a': 1, 'b': 2, 'c': 3}
# 添加
dict2 = {'d': 4}
dict1.update(dict2)
# 删除
dict1.pop('a')
# 更新
dict1['b'] = 6
# 清空
dict1 = {}
# 2.写两个集合,&,|,^,-操作
a_set = set([1, 2, 3])
b_set = set([2, 3, 4, 5])
print(a_set & b_set)
print(a_set | b_set)
print(a_set ^ b_set)
print(b_set - a_set)