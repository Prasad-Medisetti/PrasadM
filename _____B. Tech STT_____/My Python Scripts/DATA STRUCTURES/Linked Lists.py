#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 13:59:31 2020

@author: prasadm

DATA STRUCTURES - LINKED LIST 
"""

class Node:
	def __init__(self, value=None):
		self.value = value
		self.next = None
		
	def isempty(self):
		return (self.value==None)

	def append(self,v):
		if self.isempty():
			self.value = v
		elif self.next==None:
			nn = Node(v)
			self.next = nn
		else:
			(self.next).append(v)
	
	def insertb(self,v):
		if self.isempty():
			self.value = v
		else:
			nn = Node(v)
			(self.value,nn.value) = (nn.value,self.value)
			(self.next,nn.next) = (nn,self.next)
	
	def reverse(self):
		if self.isempty():
			print('List is Empty...')
			return
		elif self.next==None:
			return 
		else:
			nn = Node(self.value)
			temp = self
			while(temp.next!=None):
				nn.insertb(temp.next.value)
				temp.next = temp.next.next
			(self.value,nn.value) = (nn.value,self.value)
			(self.next,nn.next) = (nn.next,self.next)
			
	
	def deletei(self,v):
		if self.isempty():
			print('List is Empty...')
			return
		elif self.value==v:
			if self.next==None:
				self.value = None
				return
			else:
				self.value = self.next.value
				self.next = self.next.next
				return
		else:
			temp = self
			while temp.next!=None:
				if temp.next.value==v:
					temp = temp.next
					return
				else:
					temp = temp.next
			else:
				print('No %d in List'%v)
	
	def deleter(self):
		if self.isempty():
			print('List is Empty...')
		elif self.next==None:
			if self.value!=None:
				print (self.value,'is deleted...')
				self.value = None
			return
		elif (self.next).next==None:
			print((self.next).value,'is deleted...')
			self.next = None
			return
		else:
			(self.next).deleter()
	
	def show(self):
		if self.isempty():
			print('List is Empty...')
		elif self.next==None:
			print(self.value,end=' ')
			return
		else:
			print(self.value,end=' ')
			(self.next).show()
				
if __name__=='__main__':
	ll = Node()
	ll.append(100)
	ll.append(200)
	ll.append(300)
	ll.show()
	print('\nReversed')
	ll.reverse()
	temp = ll
	while(temp.value):
	    print(temp.value)
	    temp = temp.next
	    if temp==None:
	        break
	
	
	
	
# =========================================================================
