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


# ================================  bubble sort  ============================
@fn_timer
def bubble_sort(para_list):
	for i in range(len(para_list)):
		for j in range(len(para_list)-i-1):
			if para_list[j] > para_list[j+1]:
				para_list[j], para_list[j+1] = para_list[j+1], para_list[j]

bubble_sort(copy.copy(n_list))
# ====================================  end  ================================


# ============================  improrved bubble sort  ======================
@fn_timer
def bubble_sort_with_flag(para_list):
	for i in range(len(para_list)):
		flag = 0
		for j in range(len(para_list)-i-1):
			if para_list[j] > para_list[j+1]:
				para_list[j], para_list[j+1] = para_list[j+1], para_list[j]
				flag = 1 		# exchanged

bubble_sort_with_flag(copy.copy(n_list))


@fn_timer
def bubble_sort_with_pos(para_list):
	i = len(para_list)-1
	while i > 0 :
		pos = 0
		for j in range(i):
			if para_list[j] > para_list[j+1]:	
				para_list[j], para_list[j+1] = para_list[j+1], para_list[j]
				pos = j			# record the last exchange postion
		i = pos

bubble_sort_with_pos(copy.copy(n_list))


@fn_timer
def bubble_sort_binary(para_list):
	for i in range(len(para_list)):
		for j in range(len(para_list)-i-1):
			if para_list[j] > para_list[j+1]:
				para_list[j], para_list[j+1] = para_list[j+1], para_list[j]
		for j in range(len(para_list)-i-2)[::-1]:
			if para_list[j] >  para_list[j+1]:
				para_list[j], para_list[j+1] = para_list[j+1], para_list[j]

bubble_sort_binary(copy.copy(n_list))
# ====================================  end  ================================


# ================================  quick sort  =============================
def partition(para_list, para_low, para_high):
	key = para_list[para_low]
	while para_low < para_high:
		while para_low < para_high and para_list[para_high] >= key:
			para_high -= 1
		para_list[para_low], para_list[para_high] = para_list[para_high], para_list[para_low]
		while para_low < para_high and para_list[para_low] <= key:
			para_low += 1
		para_list[para_low], para_list[para_high] = para_list[para_high], para_list[para_low]
	return para_low
def quick_sort_index(para_list, para_low, para_high):
	if para_low < para_high:
		index = partition(para_list, para_low, para_high)
		quick_sort_index(para_list, para_low, index-1)
		quick_sort_index(para_list, index+1, para_high)
@fn_timer
def quick_sort(para_list):
	quick_sort_index(para_list, 0, len(para_list)-1)

quick_sort(copy.copy(n_list))
# ====================================  end  ================================


# ================================  heap sort  ==============================
def adjust_heap(para_list, para_i, para_size):
	lchild = 2*para_i+1
	rchild = 2*para_i+2
	max_n = para_i
	if para_i < int(para_size/2):
		if lchild < para_size and para_list[lchild] > para_list[max_n]:
			max_n = lchild
		if rchild < para_size and para_list[rchild] > para_list[max_n]:
			max_n = rchild
		if max_n != para_i:
			para_list[max_n],para_list[para_i] = para_list[para_i], para_list[max_n]
			adjust_heap(para_list, max_n, para_size)
def build_heap(para_list, para_size):
	for i in range(int(para_size/2))[::-1]:
		adjust_heap(para_list, i, para_size)
@fn_timer
def heap_sort(para_list):
	size = len(para_list)
	build_heap(para_list, size)
	for i in range(0, size)[::-1]:
		para_list[0], para_list[i] = para_list[i], para_list[0]
		adjust_heap(para_list, 0, i)

heap_sort(copy.copy(n_list))
# ====================================  end  ================================


# ================================  merge sort  =============================
def merge(para_list1, para_list2):
	i,j = 0,0
	result = []
	while i<len(para_list1) and j<len(para_list2):
		if para_list1[i] <= para_list2[j]:
			result.append(para_list1[i])
			i += 1
		else:
			result.append(para_list2[j])
			j += 1	
	return result + para_list1[i:] + para_list2[j:]
def merge_sort_recursion(para_list):
	if len(para_list) <= 1:
		return para_list
	num = int(len(para_list)/2)
	list1 = merge_sort_recursion(para_list[:num])
	list2 = merge_sort_recursion(para_list[num:])
	return merge(list1, list2)
@fn_timer
def merge_sort(para_list):
	para_list = merge_sort_recursion(para_list)

merge_sort(copy.copy(n_list))
# ====================================  end  ================================
