#coding:utf-8

#10进制转2进制
def ff(n):
    list1=[]
    result=''
    while n:
        y=n%2#取参数n除以2的余数
        n=n//2#计算商,并将商赋值给参数n,便于循环计算.
        list1.append(y)#将余数添加至列表
    while list1:#当list1为空,及条件为假时停止循环
        result+=str(list1.pop())#通过pop方法,去除list1中的最后一个元素,并将该元素通过+存入result中,正好10进制转2进制需要反向取结果.
    return result#返回结果.

#2进制转10进制,方法1
def gg(n):
    result=0
    n=str(n)#将参数转换为列表,便于截取.
    for i in range(0,len(n)):#设置i的取值范围等于0到字符串n的长度
        result=2*result+int(n[i])#算法公式,将计算结果赋值给s,便于下次计算
    return result #返回计算结果

#2进制转10进制,方法2
def hh(n):
    result=0
    n=str(n)#将参数转换为列表,便于截取.
    for i in range(0,len(n)):#设置i的取值范围等于0到字符串n的长度
        result+=int(n[i])*(2**i)#算法公式,将计算结果赋值给s,便于下次计算
    return result#返回计算结果

def xx(n,m):#n是10进制,m是2进制;
    print('--------------')
    print(ff(n))
    print('--------------')
    print('**************')
    print(gg(m))
    print('**************')


xx(99,1100011)