#!/usr/bin/python3

from stack import Stack
def div_by2(dec_num):
	s = Stack()
	while dec_num > 0:
		r = dec_num % 2
		s.push(r)
		dec_num = dec_num // 2
		
	bin_str=""
	while not s.is_empty():
		bin_str += str(s.pop())

	return bin_str
   
print(div_by2(242))
