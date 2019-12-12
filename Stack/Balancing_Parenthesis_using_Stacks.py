#!/usr/bin/python3

class Stack():
	def __init__(self):
		self.items=[]
	def push(self,item):
		self.items.append(item)
	def pop(self):
		return self.items.pop()
	def is_empty(self):
		return self.items == []
	def peek(self):
		if not self.is_empty():
			return self.items[-1]
	def get_stack(self):
		return self.items
def is_match(p1,p2):
	if p1=="{" and p2=="}":
		return True
	if p1=="<" and p2==">":
		return True
	if p1=="[" and p2=="]":
		return True
	if p1=="(" and p2==")":
		return True
	else:
		return False
def is_paren_balanced(input_string):
	s = Stack()
	is_balanced = True 
	index = 0
	while index < len(input_string) and is_balanced:
		paren=input_string[index]
		if paren in "{(<[":
			s.push(paren)
		else:
			if s.is_empty():
				is_balanced = False
			else:
				top = s.pop()
				if not is_match(top,paren):
					is_balanced =  False
		index+=1
	if s.is_empty() and is_balanced:
		return True
	else:
		return False

print(is_paren_balanced(input("Enter a string of Parenthesis:-")))
