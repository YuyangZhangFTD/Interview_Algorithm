"""
	integer dividing
	input:	6
	output: 6;
		5+1;
		4+2, 4+1+1;
		3+3, 3+2+1, 3+1+1+1;
		2+2+2, 2+2+1+1, 2+1+1+1+1;
		1+1+1+1+1+1.
		so, p(6)=11
"""
def q(n,m):
	if n<1 or m<1:
		return 0
	if n==1 or m==1:
		return 1
	if n< m:
		return q(n,n)
	if n==m:
		return q(n,m-1)+1
	return q(n,m-1)+q(n-m,m)
def p(n):
	return q(n,n)

print(p(6))		# ans:	p(6)=11


