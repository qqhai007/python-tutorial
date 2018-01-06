# 第一章 Python简介

## 1.1运行python
ctrl+z 退出 或 raise SystemExit
## 1.2 变量与算数表达式
```python
principal=1000
rate=0.05
numyears=5
year=1
while year<=numyears:
    printcipal=principal*(1+rate)
    print year,printcipal
    year+=1

#输出
#1 1050.0
#2 1050.0
#3 1050.0
#4 1050.0
#5 1050.0
```
python是一种动态类型语言，可以将变量名绑定不同的值（scala是静态类型？）
python打印格式化字符串
```python
print "%3d %0.2f" %(1980,22.56)
print format(1980,"3d"),format(22.56,"0.2f")
print "{0:3d} {1:0.2f}".format(1980,22.56)
```
## 1.3 条件语句
```python
a=0
b=1

if a<b:
    print "Computer say yes"
else:
    print "Computer say no"
# 可用or,and,not 关键字
if a==b or 1==2 and not a:
    print "aaaa"
    
#python 没有switch case
if a==1:
    print 'a'
elif a==2:
    print 'b'
elif a==3:
    print 'c'
else:
    print 'd'
```
## 1.4 文件输入与输出
```python
f=open("foo.txt")
line=f.readline()
while line:
    print line,#后面跟‘，’,将忽略换行
    line=f.readline()
f.close()
```
## 1.5 字符串
单引号，双引号或三引号（可以跨行）
切片和索引
str(),repr(),format进行字符串转换
```python
s="""hello 
wooeselk
sadf;d"""
s[0]
s[3:5]
x=3.4
str(x)
repr(x)
format(x,"4d")
```
## 1.6 列表
```python
names=['Dave','Mark','Ann','Phil']
a=names[2]
names[0]='Jeff'
names[0:2]
names=list()
a=[1,2,3]+[4,5]
names.append("paula")
names.insert(2,"thomas")
fvalues=[float(line) for line in lines]
```
## 1.7 元组
```python
stock=('good',100,34.5)
a=()
a=tuple()
```
## 1.8 集合

```python
s=set(['a','b','c'])
t=set("abc")
#s==t
a=t|s #并集
b=t&s #交集
c=t-s #补集
d=t^s #对称差集 （项在t或s中，但不会在二者同时出现)
t.add('x')
s.update([10,37,42])
```
## 1.9 字典
```python
stock={"name":'good','share':100}
a={}
a=dict()
```

## 1.10 迭代与循环
```python
for n in [1,2,3]:
    print n

for n in range(1,10):
    print n

#xrange() 避免内存问题 python3 用range()
```
## 1.11函数
```python
def remainder(a,b):
    return a+b
```
## 1.12 生成器
```python
def countdown(n):
    print "countdown"
    while n>0:
        yield n
        n-=1

c=countdown(5)
c.next()
```

## 1.13 协程
```python
def print_matcher(matchtext):
    print "looking for",matchtext
    while True:
        line=(yield)
        if matchtext in line:
            print line

matcher=print_matcher("python")
matcher.next()
matcher.send("hello python")
matcher.send("hello python 222")
matcher.close()
```

## 1.14 对象与类
```python
class Stack(object):
    def __init__(self):
        self.stack=[]
    def push(self,object):
        self.stack.append(object)
    def pop(self):
        return self.stack.pop()
    def length(self):
        return len(self.stack)
    
s=Stack()
s.push('a')
print s.pop()
print s.length()
```
## 1.17 获得帮助
```python


```


