content = '   my name is ben   '
#分别去掉左边,右边,两端空格
print(content)
contentNew = content.strip()
print(contentNew)
#将content去掉两端空格后与',my age is 19'拼接
contentNew1 = contentNew + ',my age is 19'
print(contentNew1)
#分别用index查找'my'和用find查找'name'
myHasByIndex = contentNew1.index('my')
print(myHasByIndex)
myHasByFind = contentNew1.find('name')
print(myHasByFind)

#判断'my'是否存在于content;然后判断't'是否存在
myIfCon = content.index('my')
print(myIfCon)
tIfCon = content.find('t')
print(tIfCon)

#将content首先转换大写,然后转换为小写,最后标题化
contentUpper = content.upper()
print(contentUpper)
contentLower = contentUpper.lower()
print(contentLower)
contentTitle = contentLower.title()
print(contentTitle)

#截取索引从4开始到结尾的字符子串
print(content[4:])

#讲content按空格切分
print(content.split())

#用':'连接[1,2,3]
listStr = ["1","2","3"]
website = ':'.join(listStr)
print(website)