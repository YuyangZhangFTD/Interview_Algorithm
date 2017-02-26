"""
	search algorithm
	search a value in a list, return the index
"""
import random
import time
import copy
from functools import wraps


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
v_search = random.randint(1,20000)


# ====================  build in function for search  =========================
@fn_timer
def build_in_search(para_list, para_value):
	try:
		return para_list.index(para_value)
	except:
		return -1
print(build_in_search(copy.copy(n_list), v_search))
# ================================  end  ======================================


# ============================  sequence search  ==============================
@fn_timer
def sequence_search(para_list, para_value):
	for i in range(len(para_list)):
		if para_list[i] == para_value:
			return i
	else:
		return -1
print(sequence_search(copy.copy(n_list), v_search))
# =================================  end  =====================================


# ============================  binary search  ================================
@fn_timer
def binary_search(para_list, para_value):
	# binary search need sorted list
	para_list.sort()
	low = 0
	high = len(para_list)-1
	while low <= high:
		mid = int((low+high)/2)
		if para_list[mid] == para_value:
			return mid
		if para_list[mid] > para_value:
			high = mid-1
		if para_list[mid] < para_value:
			low = mid+1
	else:
		return -1
print(binary_search(copy.copy(n_list), v_search))


def binary_search_index(para_list, para_value, low, high):
	mid = int((low+high)/2)
	if para_list[mid] == para_value:
		return mid
	if para_list[mid] > para_value:
		return binary_search_index(para_list, para_value, low, mid-1)	
	if para_list[mid] < para_value:
		return binary_search_index(para_list, para_value, mid+1, high)
	if low >= high:
		return -1
@fn_timer
def binary_search_recursion(para_list, para_value):
	para_list.sort()
	low = 0
	high = len(para_list)-1	
	return binary_search_index(para_list, para_value, low, high)
print(binary_search_recursion(copy.copy(n_list), v_search))
# =================================  end  =====================================


# =========================== insertion search  ===============================
@fn_timer
def insertion_search(para_list, para_value):
	para_list.sort()
	low = 0
	high = len(para_list)-1
	while low < high:
		mid = low + int((para_value - para_list[low]) / (para_list[high]-para_list[low]))
		if para_list[mid] == para_value:
			return mid
		elif para_list[mid] > para_value:
			high = mid - 1
		elif para_list[mid] < para_value:
			low = mid + 1
	else:
		return -1
print(insertion_search(copy.copy(n_list), v_search))
# =================================  end  =====================================


# =============================  tree search  =================================
# TODO
# =================================  end  =====================================


# =============================  hash search  =================================
# TODO
# =================================  end  =====================================
