"""
	The count-and-say sequence is the sequence of integers beginning as follows:
	|-------|--------------------|-------------------|
	| input	|	output	    	 |	 description 	 |
	|-------|--------------------|-------------------|
	|   1   |         11	     |      1 '1	 	 |
	|   2   |         21         |      2 '1's 		 |
	|   3   |        1211        |     1 '2', 2 '1's |
	|   4   |        1231        |     1 '2', 3 '1's |
	|-------|--------------------|-------------------|
"""
def countAndSay(n):
	if n==0:
		return "1"
	string = "1"
	while n>0 :
		tmp = ""
		count_list = [string.count(str(num)) for num in range(10)]
		for i in range(10)[::-1]:
			if count_list[i] == 0:
				continue
			tmp += str(count_list[i]) + str(i)
		string = tmp
		n -= 1
	return string

print(countAndSay(3))
print(countAndSay(4))
