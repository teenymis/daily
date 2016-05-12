#coding:utf-8
# 最大公约数

#各种失败:
# from math import sqrt---说明,为提高效率使用.但忽略了小于平方根的约数.
# def ff(n,m):
#     list1=[]
#     for i in range(int(sqrt(n)),n+1):
#         if n%i==0:
#             list1.append(i)
#     list2=[]
#     for j in range(int(sqrt(m)),m+1):
#         if m%j==0:
#             list2.append(j)
#     list3=[eache1+'.'+eache2 for eache1 in list1 for eache2 in list2 if eache1[0]==eache2[0]]
#     print(list3)
#
# ff(100,150)

#list3=[(int(k1),int(k2)) for k1 in list1 for k2 in list2 if int(k1[0])==int(k2[0])]
# list3=[]
# print(list1)
# print(list2)
# print(list3)

#成功1次,对于很大的数,运行效率级低.
def ff(n,m):
    list1=[i for i in range(1,n+1) if n%i==0]#计算参数1的所有公约数
    list2=[j for j in range(1,m+1) if m%j==0]#计算参数2的所有公约数
    list3=[]
    for k1 in range(0,len(list1)):#将参数1,参数2相等的公约数形成列表
        for k2 in range(0,len(list2)):
            if list1[k1]==list2[k2]:
                list3.append(list1[k1])
    return max(list3)#返回最大的列表值
print ff(123456,7890)


#查看答案后改进:
# http://baike.baidu.com/view/255668.htm 辗转相除法:
'''
设两数为a、b(a>b)，求a和b最大公约数(a，b)的步骤如下：用a除以b，得a÷b=q......r1(0≤r1)。若r1=0，则(a，b)=b；
若r1≠0，则再用b除以r1，得b÷r1=q......r2 (0≤r2）.若r2=0，则(a，b)=r1，
若r2≠0，则继续用r1除以r2，……如此下去，直到能整除为止。其最后一个为被除数的余数的除数即为(a, b)。
例如：a=25,b=15，a/b=1......10,b/10=1......5,10/5=2.......0,最后一个为被除数余数的除数就是5,5就是所求最大公约数。
'''

def fg(m,n):
    while n:#t的值赋给y,当y==0,0在这里代表False
        t=m%n#获取余数
        m=n#交换值,把除数交换成被除数
        n=t#交换至,将余数交换成除数
    return m#当余数=0时,最大公约数就是被除数
print fg(1234567890,7890123456)












