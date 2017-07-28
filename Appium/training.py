#-*- coding:utf8 -*-
#coding=utf-8

#list training
# months=['January','February','March','April','May','June','July','August','September','October','November','December']
# endings=['st','nd','rd']+17*['th']+['st','nd','rd']+7*['th']+['st']
# years=raw_input('Year: ')
# month=raw_input('Month: ')
# day=raw_input('Day: ')
# month_number=int(month)-1
# day_number=int(day)-1
# print months[month_number]+' '+day+endings[day_number]+', '+years


# a=[1,2,3]
# b=[4,5,6]
# print a+b
# print a
# a.extend(b)
# print a
# print b
#
# x=[4,3,2]
# # print x.pop()
# # # print x.remove(1)
# # x.reverse()
# # print x
# # y=x[:]
# # print y
# # y.sort()
# # print y
# # # print x
# # print cmp(9,10)
# # x.sort(cmp)
# # print x

#String format

# format="hello %s !"
# value='world'
# print format %value

# sep=["1","2"]
# seq="+"
# print seq.join(sep)

# print "wanngyu".replace('yu','wang')

#print "1+2+3+4+5".split('+')

#print " a bc ".strip()

# d={'name':'A','age':10}
# print len(d)
# print d['name']
# d['name']='B'
# print d['name']
#
# del d['name']
# print d
#
# print 'name'in d



# people={'Alice':{'phone':'1111','addr':"Alice's addr"},
#         'Beth':{'phone':'2222','addr':"Beth's addr"},
#         'Cecil':{'phone':'3333','addr':"Cecil's addr"}
#         }
# labels={'phone':'phone number','addr':'address'}
# if request=='p':key='phone'
# if request=='a':key='addr'
# name=raw_input("input name")
# print people[name][key]



#
# from copy import deepcopy
# d={'name':'aa','age':['12','13']}
# b=deepcopy(d)
# b['age'].remove('12')
# print "b=%s" % b
#

# print dict.fromkeys(['name','age'],['A','B'])
#
# d={}
# print d.fromkeys(['phone'],['123'])
#
# print d.get('phone')
#
# print a('name')

# people={'Alice':{'phone':'1111','addr':"Alice's addr"},
#         'Beth':{'phone':'2222','addr':"Beth's addr"},
#         'Cecil':{'phone':'3333','addr':"Cecil's addr"}
#         }

# num=input("input a number:")
# if num >0:
#         print 'num > 0'
# elif num<0:
#         print 'num < 0'
# else:
#         print 'num is 0'





#input和rawinput的区别
# A=raw_input('raw_input 输入：')
# B=input('input 输入：')
#
# C=raw_input('raw_input:')
# D=input('input:')
# print "raw_input's %s" %type(C)
# print "input's %s" %type(D)





#
#
# for number in range(1,101):
#     print number
#
#
# d={'x':1,'y':2,'z':3}
# for key in d:
#     print key ,"=",d[key]
#



# names=['A','B','C']
# ages=[1,2,3]
# zip(names,ages)
# for name,age in zip(names,ages):
#     print name ,age





#
# while True:
#     word=raw_input("input words:")
#     if not word:
#         break
#     else:
#         print word
#
#



# x=1
# y=x
# print y
# y=2
# print x
# print y


#  del 使用

# x=[1,2]
# y=x
# y[1]=3
# print x
# print y

#
# def change(n):
#     n[0]='AAA'
#     print n
# name=['BBB','CCC']
# change(name)
# print name

# def change(n):
#     n='AAA'
#     print n
# names='BBB'
# change(names)
# print names


#
# def change(n):
#     n=['AAA']
# name=['BBB']
# change(name[:])
# print name



# storage={}
# storage['first']={}
# storage['middle']={}
# storage['last']={}
# me='Mangus Lie Hetland'
# storage['first']['Mangus']=me
# storage['middle']['Lie']=me
# storage['last']['Hetland']=me
# print storage['first']['Mangus']
#




# dic={'key1':'value','key2':'value2','key3':['value3-1','value3-2']}
#
# dic['key1']='values'
# print dic['key1']

#
# #########按名字找全名###########
# def init(data):
#     data['first']={}
#     data['middle']={}
#     data['last']={}
#
# def store(data,*full_names):
#     for full_name in full_names:
#         names=full_name.split()
#         if names==2:
#            names.insert('1',)
#         labels='first','middle','last'
#         for label,name in zip(labels,names):
#            people=lookup(data,label,name)
#            if people:
#                people.append(full_name)
#            else:
#                data[label][name]=[full_name]
#
# def lookup(data,label,name):
#     return data[label].get(name)
#
# myname={}
# init (myname)
# store(myname,'Magus Lie Hetland','Ann Mdie Deww')
# print lookup(myname,'first','Ann')


#######收集参数########
# def printparams(x,y,z=1,*pospar,**keyspar):
#     print x,y,z
#     print pospar
#     print keyspar
#
#
#
# printparams(5,6,A=3,B=4)    print x,y,z
#     print pospar
#     print keyspar
#


########过程反转###########
#########星号只在定义函数（允许多个参数），调用函数（分裂字典或元组）时有效。############
# def hello3(greeting='hello',name='zhangsan'):
#     print '%s,%s'%(greeting,name)
#
# params={'greeting':'wellmet','name':'Mrs.Wang'}
# hello3(**params)


# def recurion():
#     return recurion()


# class Class():
#     def method(self):
#         print 'I have self'
# def funcation():
#     print "I don't"
#
#
# instance=Class()
# instance.method()
# instance.method=funcation
# instance.method()


# def functaiontest():
#     print 'A'
#
# functaiontest
#




# class Secrective():
#     def __inaccessible(self):
#         print 'bet you cannot see me...'
#     def accessible(self):
#         print 'the secrect message is...'
#         self.__inaccessible()
#
#
# s=Secrective()
# #s.__inaccessible()
# s.accessible()



#-*- coding:utf8 -*-
#coding=utf-8

#list training
# months=['January','February','March','April','May','June','July','August','September','October','November','December']
# endings=['st','nd','rd']+17*['th']+['st','nd','rd']+7*['th']+['st']
# years=raw_input('Year: ')
# month=raw_input('Month: ')
# day=raw_input('Day: ')
# month_number=int(month)-1
# day_number=int(day)-1
# print months[month_number]+' '+day+endings[day_number]+', '+years


# a=[1,2,3]
# b=[4,5,6]
# print a+b
# print a
# a.extend(b)
# print a
# print b
#
# x=[4,3,2]
# # print x.pop()
# # # print x.remove(1)
# # x.reverse()
# # print x
# # y=x[:]
# # print y
# # y.sort()
# # print y
# # # print x
# # print cmp(9,10)
# # x.sort(cmp)
# # print x

#String format

# format="hello %s !"
# value='world'
# print format %value

# sep=["1","2"]
# seq="+"
# print seq.join(sep)

# print "wanngyu".replace('yu','wang')

#print "1+2+3+4+5".split('+')

#print " a bc ".strip()

# d={'name':'A','age':10}
# print len(d)
# print d['name']
# d['name']='B'
# print d['name']
#
# del d['name']
# print d
#
# print 'name'in d



# people={'Alice':{'phone':'1111','addr':"Alice's addr"},
#         'Beth':{'phone':'2222','addr':"Beth's addr"},
#         'Cecil':{'phone':'3333','addr':"Cecil's addr"}
#         }
# labels={'phone':'phone number','addr':'address'}
# if request=='p':key='phone'
# if request=='a':key='addr'
# name=raw_input("input name")
# print people[name][key]



#
# from copy import deepcopy
# d={'name':'aa','age':['12','13']}
# b=deepcopy(d)
# b['age'].remove('12')
# print "b=%s" % b
#

# print dict.fromkeys(['name','age'],['A','B'])
#
# d={}
# print d.fromkeys(['phone'],['123'])
#
# print d.get('phone')
#
# print a('name')

# people={'Alice':{'phone':'1111','addr':"Alice's addr"},
#         'Beth':{'phone':'2222','addr':"Beth's addr"},
#         'Cecil':{'phone':'3333','addr':"Cecil's addr"}
#         }

# num=input("input a number:")
# if num >0:
#         print 'num > 0'
# elif num<0:
#         print 'num < 0'
# else:
#         print 'num is 0'





#input和rawinput的区别
# A=raw_input('raw_input 输入：')
# B=input('input 输入：')
#
# C=raw_input('raw_input:')
# D=input('input:')
# print "raw_input's %s" %type(C)
# print "input's %s" %type(D)





#
#
# for number in range(1,101):
#     print number
#
#
# d={'x':1,'y':2,'z':3}
# for key in d:
#     print key ,"=",d[key]
#



# names=['A','B','C']
# ages=[1,2,3]
# zip(names,ages)
# for name,age in zip(names,ages):
#     print name ,age





#
# while True:
#     word=raw_input("input words:")
#     if not word:
#         break
#     else:
#         print word
#
#



# x=1
# y=x
# print y
# y=2
# print x
# print y


#  del 使用

# x=[1,2]
# y=x
# y[1]=3
# print x
# print y

#
# def change(n):
#     n[0]='AAA'
#     print n
# name=['BBB','CCC']
# change(name)
# print name

# def change(n):
#     n='AAA'
#     print n
# names='BBB'
# change(names)
# print names


#
# def change(n):
#     n=['AAA']
# name=['BBB']
# change(name[:])
# print name



# storage={}
# storage['first']={}
# storage['middle']={}
# storage['last']={}
# me='Mangus Lie Hetland'
# storage['first']['Mangus']=me
# storage['middle']['Lie']=me
# storage['last']['Hetland']=me
# print storage['first']['Mangus']
#




# dic={'key1':'value','key2':'value2','key3':['value3-1','value3-2']}
#
# dic['key1']='values'
# print dic['key1']

#
# #########按名字找全名###########
# def init(data):
#     data['first']={}
#     data['middle']={}
#     data['last']={}
#
# def store(data,*full_names):
#     for full_name in full_names:
#         names=full_name.split()
#         if names==2:
#            names.insert('1',)
#         labels='first','middle','last'
#         for label,name in zip(labels,names):
#            people=lookup(data,label,name)
#            if people:
#                people.append(full_name)
#            else:
#                data[label][name]=[full_name]
#
# def lookup(data,label,name):
#     return data[label].get(name)
#
# myname={}
# init (myname)
# store(myname,'Magus Lie Hetland','Ann Mdie Deww')
# print lookup(myname,'first','Ann')


#######收集参数########
# def printparams(x,y,z=1,*pospar,**keyspar):
#     print x,y,z
#     print pospar
#     print keyspar
#
#
#
# printparams(5,6,A=3,B=4)    print x,y,z
#     print pospar
#     print keyspar
#


########过程反转###########
#########星号只在定义函数（允许多个参数），调用函数（分裂字典或元组）时有效。############
# def hello3(greeting='hello',name='zhangsan'):
#     print '%s,%s'%(greeting,name)
#
# params={'greeting':'wellmet','name':'Mrs.Wang'}
# hello3(**params)


# def recurion():
#     return recurion()


# class Class():
#     def method(self):
#         print 'I have self'
# def funcation():
#     print "I don't"
#
#
# instance=Class()
# instance.method()
# instance.method=funcation
# instance.method()


# def functaiontest():
#     print 'A'
#
# functaiontest
#




# class Secrective():
#     def __inaccessible(self):
#         print 'bet you cannot see me...'
#     def accessible(self):
#         print 'the secrect message is...'
#         self.__inaccessible()
#
#
# s=Secrective()
# #s.__inaccessible()
# s.accessible()





#
# class MemberCounter:
#     members=0
#     def init(self):
#         MemberCounter.members+=1
#
# m1=MemberCounter()
# m1.init()
# print MemberCounter.members
# m2=MemberCounter()
# m2.init()
# print MemberCounter.members

#
# try:
#     x=input('input your first number:')
#     y=input('input your second number:')
#     z=x/y
#     print format(z)
# except(ZeroDivisionError,TypeError,NameError),e:
#     print 'your numbers are bogus...'
#     print e


#
# Exception
#
# while True:
#     try:
#        x=input('input your first number:')
#        y=input('input your second number:')
#        print x/y
#     except:
#         print 'invalid'
#     else:
#         break

# try:
#     x=1/2
# except ZeroDivisionError:
#     print 'unknown variable'
# else:
#     print'no error'
# finally:
#     print 'cleaning'
#

# class Foobar:
#     def __init__(self,value):
#         self.somevar=value
#
#
# f=Foobar('This is Constructor argument')
# print f.somevar





# __metaclass__=type
# class Bird:
#     def __init__(self):
#         self.hungry=True
#     def eat(self):
#         if self.hungry:
#             print 'Aaaaa..'
#             self.hungry=False
#         else:
#             print 'No Thanks'
#
# class SingBird(Bird):
#     def __init__(self):
#         self.sound='Guagua'
#         super(SingBird,self).__init__()
#     def sing(self):
#         print self.sound
#
# sb=SingBird()
# sb.sing()
# sb.eat()
# sb.eat()
#

# class Rectangle():
#     def __init__(self):
#         self.height=0
#         self.weight=0
#     def setsize(self,size):
#         self.height,self.weight=size
#     def getsize(self):
#         return self.weight,self.height
#
# r=Rectangle()
# r.height=10
# r.weight=15
# print r.getsize()
# r.setsize((100,150))
# print r.getsize()
# print r.weight


#
# class MyClass():
#     val1='value1'
#     def __init__(self):
#         val2='value2'
#     @staticmethod
#     def staticmd():
#         print '静态方法，无法访问val1和val2'
#     @classmethod
#     def classmd(cls):
#         print '类方法：'+str(cls)+'val1:'+cls.val1+',无法访问val2'
#     def testval1(self):
#         print self.val1
#
# mc=MyClass()
# mc.staticmd()
# mc.classmd()
# MyClass.classmd()
# MyClass.staticmd()
# mc.val1='Value Changed'
# print mc.val1
# mc.classmd()
# MyClass.classmd()
# MyClass.val1='class value changed'
# MyClass.classmd()
# mc.testval1()
# mc

#
# from collections import Iterator,Iterable
# print isinstance((),Iterator)
#
#
# print  isinstance((),Iterable)



# g=(x*x for x  in range(10))
# for n in g:
#     print n


# def odd():
#     print 'step 1'
#     yield 1
#     print 'step 2'
#     yield 2
#     print 'step 3'
#     yield 3
#
#
# d=odd()
# next(d)
# next(d)
# next(d)


# def fib(max):
#     n,a,b=0,0,1
#     while n<max:
#         yield b
#         a,b=b,a+b
#         n=n+1
#     return 'done'
#
# f=fib(6)
# while True:
#     try:
#         x=next(f)
#         print (x)
#     except StopIteration as e:
#         print ('Generator return value:',e.value)
#         break


# import copy
# # print [n for n in dir(copy) if not n.startswith('_')]
# print copy.__all__
#
# print range.__doc__

# b=set([1,2,3])
# a=set([4,5])
# a.add(frozenset(b))
# print a
#
# from heapq import *
# heap=[9,3,6,2,6,8]
# heapify(heap)
# print heap
# heapreplace(heap,0.5)
# print heap
#
# from collections import deque
# q=deque(range(5))
# q.append(5)
# q.appendleft(6)
# q.popleft()
# print q
# # q.rotate()
# # print q
# # q.rotate(-2)
# q.extend([6,7])
# q.extendleft([0.5])
# print q

# from random import *
# print random()

# import shelve
# s=shelve.open('test.db')
# s['x']=['a','b','c']
# print s['x']


# import shelve
# def store_person(db):
#     pid=raw_input('Enter unique ID:')
#     person={}
#     person['name']=raw_input('enter name:')
#     person['age']=raw_input('enter age:')
#     person['phone']=raw_input('enter phone:')
#     db[pid]=person
#
# def lookup_person(db):
#     pid=raw_input('Enter unique ID:')
#     field=raw_input('what you want to know(name,age,phone)?:')
#     field_low=field.strip().lower()
#     print field.capitalize()+':',db[pid][field_low]
#
# def print_help():
#     print 'The available cmd is :'
#     print 'Store:Store information about person'
#     print 'Lookup:Lookup a person from unique ID'
#     print 'Quit:Save changes and exit'
#     print '?:Print this message'
#
# def enter_command():
#     cmd=raw_input('enter command(? for help):')
#     return cmd.strip().lower()
#
# def main():
#     database=shelve.open('database.dat')
#     try:
#         while True:
#             cmd=enter_command()
#             if cmd=='store':
#                 store_person(database)
#             elif cmd=='lookup':
#                 lookup_person(database)
#             elif cmd=='?':
#                 print_help()
#             elif cmd== 'quit':
#                 return
#     finally:
#         database.close()
# if __name__=='__main__':main()

# f=open('test.rtf','w')
# f.write('hello')
# f.write('world')
# f.close()
# f=open('test.rtf','r')
# print f.read(4)
# print f.read()

# import sys
# text=sys.stdin.read()
# words=text.split()
# wordcount=len(words)
# print wordcount
#
# cat somefile.txt | python training.py

#f=open('testfile.txt')
#print f.readline()
# for i in range(3):
#     print str(i)+':'+f.readline()
# f.write('123')
# f.close()
# f=open('somefile.txt')
# print f.readlines()
# f.close()
# lines=f.readlines()
# lines[1]="is not \n"
# f.close()
# f=open('somefile.txt','w')
# f.writelines(lines)
# f.close()
# f=open('somefile.txt')
# print f.readline()
# f.close()
# f=open('testfile.txt','w')
# f.write('First line\n')
# f.write('second line\n')
# f.write('third line\n')
# f.close()
# lines=list(open('testfile.txt'))
# print lines
# first,second,third=open('testfile.txt')
# print first,second,third
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('http://www.baidu.com/')


#
# from nose.tools import assert_equal
# from parameterized import parameterized
# import HtmlTestRunner
# import unittest
# import math

# class TestMathUnitTest(unittest.TestCase):
#     @parameterized.expand([
#         ("negative", -1.5, -2.0),
#         ("integer", 1, 1.0),
#         ("large fraction", 1.6, 1),
#     ])
#     def test_floor(self, name, a, b):
#         print a+b
#
# if __name__ == "__main__":
#     unittest.main()

# def hello():
#     num=1
#     return num
#
# print hello()


#
# class test():
#     @staticmethod
#     def testvalue():
#         a='test'
#         print a
#         return a
#
# print a

#继承和多态
# class person(object):
#     def __init__(self,name,sex):
#         self.name=name
#         self.sex=sex
#
#     def print_info(self):
#         print self.name
#         print self.sex
#
# class childs(person):
#     def __init__(self,name,sex,age):
#         #person.__init__(self,name,sex)
#         super(childs,self).__init__(name,sex)
#         self.age=age
#     def print_info(self):
#         print self.age
#
# May=childs('May','female','20')
# May.print_info()



class person(object):
    def __init__(self):
        pass
    def printtitle(self):
        print 'this is person'

class girl(person):
    def __init__(self):
        pass
    def printtitle(self):
        print 'this is a girl'


class boy(person):
    def __init__(self):
        pass


girls=girl()
girls.printtitle()
boys=boy()
boys.printtitle()




















