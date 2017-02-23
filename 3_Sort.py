"""
	sort 
	input:	an unsorted list
	output:	a sorted list
"""
import time
import random
from functools import wraps
import copy

# record time
def fn_timer(function):
	@wraps(function)
	def function_timer(*args, **kwargs):
		start = time.clock()
		result = function(*args, **kwargs)
		end = time.clock()
		print('%s use time:  %s'%(function.__name__, str(end-start)))
		return result
	return function_timer
		


# generate an unsorted list
n_list = [random.randint(1,20000) for __ in range(10000)]


# build-in sort function
@fn_timer
def build_in_sort(para_list):
	para_list.sort()
build_in_sort(copy.copy(n_list))



# straight_insertion_sort
@fn_timer
def straight_insertion_sort(para_list):
	for i in range(1, len(para_list)):
		key = para_list[i]
		for j in range(i):
			if key < para_list[j]:
				while i!=j:
					para_list[i] = para_list[i-1]
					i -= 1
				para_list[j] = key
				break
straight_insertion_sort(copy.copy(n_list))



# shell's sort
@fn_timer
def shell_sort(para_list):
	pass







