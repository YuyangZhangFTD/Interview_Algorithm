"""
	sort 
	input:	an unsorted list
	output:	a sorted list
"""
import time
import random
from functools import wraps
import copy
import math

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


# ==========================  build-in sort function  ========================
@fn_timer
def build_in_sort(para_list):
	para_list.sort()
build_in_sort(copy.copy(n_list))
# ===================================  end  ==================================


# ==========================  straight_insertion_sort  =======================
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
# =====================================  end  ================================


# ====================================  shell's sort  ========================
def shell_insertion_sort(para_list, para_dk):
	for i in range(para_dk, len(para_list)):
		key = para_list[i]
		if key  < para_list[i-para_dk]:
			j = i - para_dk
			while key < para_list[j]:
				para_list[i] = para_list[i-para_dk]
				j -= para_dk
				if j<0:
					break
			para_list[j+para_dk] = key
@fn_timer
def shell_sort(para_list):
	dk = math.floor(len(para_list)/2)
	while dk >= 1: 
		shell_insertion_sort(para_list, dk)
		dk = int(dk/2)
shell_sort(copy.copy(n_list))
# ====================================  end  ================================
	
# ============================  simple selection sort  ======================
@fn_timer
def simple_selection_sort_with_BIF(para_list):	# with build-in function: min()
	for i in range(1, len(para_list)):
		min_num = min(para_list[i:])
		min_index = para_list[i:].index(min_num)+i
		if para_list[i-1] > para_list[min_index]:
			para_list[i-1], para_list[min_index] = para_list[min_index], para_list[i-1]
def get_min(para_list):				# get the index of min number
	index = 0
	for i in range(1, len(para_list)):
		if para_list[index] > para_list[i]:
			index = i	
	return index
@fn_timer
def simple_selection_sort(para_list):		# min() by myself
	for i in range(1, len(para_list)):
		min_index = get_min(para_list[i:])+i
		if para_list[i-1] > para_list[min_index]:
			para_list[i-1], para_list[min_index] = para_list[min_index], para_list[i-1]
simple_selection_sort_with_BIF(copy.copy(n_list))
simple_selection_sort(copy.copy(n_list))
# ====================================  end  ================================

# ===========================  binary selection sort ========================
def get_max_min(para_list):
	max_index = 0
	min_index = 0
	for i in range(1, len(para_list)):
		if para_list[max_index] < para_list[i]:
			max_index = i
		if para_list[min_index] > para_list[i]:
			min_index = i
	return max_index, min_index
@fn_timer
def binary_selection_sort(para_list):
	for i in range(1, int(len(para_list)/2)):
		max_index, min_index = get_max_min(para_list[i:-i])
		max_index += i
		min_index += i
		if para_list[i-1] > para_list[min_index]:
			para_list[i-1], para_list[min_index] = para_list[min_index], para_list[i-1]
		if para_list[-i] < para_list[max_index]:
			para_list[-i], para_list[max_index] = para_list[max_index], para_list[-i]
binary_selection_sort(copy.copy(n_list))
# ====================================  end  ================================

# ================================  heap sort  ==============================
# TODO
# ====================================  end  ================================

# ================================  bubble sort  ============================
# TODO
# ====================================  end  ================================

# ================================  quick sort  =============================
# TODO
# ====================================  end  ================================



