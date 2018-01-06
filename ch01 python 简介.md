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

