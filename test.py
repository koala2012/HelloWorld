#!/usr/bin/env python
#coding=utf8

import os,sys,time

pid = os.fork()
print pid
if pid>0:
	sys.exit(0)

print ('come here')


def test(L=None):
	if L is None:
		L=[]
	L.append('test')
	print L

test()
test()

def func(*args,**kw):
	print 'args=',args, 'kw=',kw

def wai_hansu(pram1):
	def nei_hansu(pram2):
		return pram1*pram2
	return nei_hansu

def zsq(func):
	def nei(*args,**kw):
		print 'before doing thing'
		func(*args,**kw)
		print 'after doing thing'
	return nei

@zsq
def login(name,test):
	print 'login...',name, test

login('wjy','greeting')

b = 10
a = lambda x:x*x+b
b = 3
print (a(2))



import a

def f():
	print 'in f'
	import a
	print 'end f'

f()
f()

list = ['a','b','c']

print list[10:]
del list[1:1]
print list



# a = wai_hansu(123)
# print a
# print a(456)


if __name__ == '__main__':
	func(1,2,4,5,yes='fuc')

