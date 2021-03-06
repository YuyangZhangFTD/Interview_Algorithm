# 面试算法题总结
- 1. Max Gap 最大间隔 
[1_MaxGap.py](https://github.com/YuyangZhangFTD/Interview_Algorithm/blob/master/1_MaxGap.py)

问题描述：给定n个无序实数x_1,x_2,...,x_n，求这n个数在实轴上相邻2个数之间最大差值，设计一个线性时间的解法。

解法分析：鸽舍原理，将其分平均为n-1段，必有一段是空的，对每一段进行线性扫描，即可求得最大间隔。

- 2. Integer Dividing 整数划分 
[2_IntegerDividing.py](https://github.com/YuyangZhangFTD/Interview_Algorithm/blob/master/2_IntegerDividing.py)

问题描述：将正整数n表示为一系列正整数之和，n=n_1+n_2+...+n_k，其中n_1>=n_2>=...>=n_k，正整数n的不同划分个数称为正整数n的划分数，记为p(n)。

解法分析：递归求解。在正整数n的所有不同划分中，将最大加数n_1不大于m的划分个数记为q(n,m)，有以下关系：

(1) q(n,1)=1,n>=1.

(2) q(n,m)=q(n,n),m>=n.

(3) q(n,n)=q(n,n-1)+1.

(4) q(n,m)=q(n,m-1)+q(n-m,m),n>m>1


- 3. Sort 排序 
[3_Sort.py](https://github.com/YuyangZhangFTD/Interview_Algorithm/blob/master/3_Sort.py)

常见排序算法总结。



- 4. Count and Say 计数并读数 
[4_CountAndSay.py](https://github.com/YuyangZhangFTD/Interview_Algorithm/blob/master/4_CountAndSay.py)

问题描述：给定一个自然数n写出第n个序列的数。

input|output|description 	
-----|------|-------------
1    | 11   |1 '1'	     
2    | 21   |2 '1's 	    
3    | 1211 |1 '2', 2 '1's 
4    | 1231 |1 '2', 3 '1's 

解法分析： 简单地计数即可。


- 5. Search 查找

常见查找算法总结。








