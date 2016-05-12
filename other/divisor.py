#coding:utf-8

'''
pcount=0
def pnum():
    global pcount
    for i in range(1,101):
        for j in range(1,i+1):
            if i%j==0:
                pcount+=1
        if pcount==2:
            print i
            pcount=0
print pnum()




#def div():

'''

from math import sqrt
list1=[ p for p in range(2, 1001) if 0 not in (p%d for d in range(2, int(sqrt(p))+1)) ]
print list1



"""
# 其他人的解题思路:
# 思路：
# 1.依次列举三角形数
# 2.取该三角形数的算术平方根
# 3.判断该算术平方根是否整数
# 4.判断该三角形数依次能被多少自然数整除，自然数范围为：range（2，算数平方根取整）
# -----------------------------------------
# 说明：
# 1.任何自然数都能被1和其本身整除。所以约束直接2起步;
# 2.如果自然数能被小于算数平方根的数整除，则必然存在有一个大于算数平方根的数整除
#    即：能被小于算数平方根的自然数整除，则必有2个约数
#    如20能被2整除，则必然能被10整除；能被4整除，则必然能被5整除
# 3.如果该三角形数的算数平方根是整数，则只增加一个约数
#    如9的算数平方根是3。则只会增加一个约数3。（3*3=9）

from math import sqrt
n=1
num=1
while True:
    n=n+1
    num=num+n
    m=2
    if int(sqrt(num))==sqrt(num):
           m-=1
    for i in range(2，int(sqrt(num))+1):
        if num%i==0:
            m=m+2
    if m>500:
        break
print(n)
print(num)
"""
