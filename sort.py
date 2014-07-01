#算法导论看到9章, 翻来覆去全是排序. 
#有印象的有, 插入, 堆排序, 归并排序, 快速排序, 计数排序? 还有中位数等等... 

import random

def test_sort(fun = None, num = 20):
	if num != None:
		num = 20
	for x in range(0, num):
		test_list = []
		for y in range(0, 20):
			test_list += [random.randrange(0, 30)]
		print("o",test_list)
		if fun != None:
			fun(test_list, 0, len(test_list) - 1)
		
		print(test_list)



#1 insert sort 
def insert_sort(alist, start, end):
	for i in range(start + 1, end + 1):
		for k in range(i, start, -1):
			if alist[k] < alist[k - 1]:
				alist[k], alist[k - 1] = alist[k - 1], alist[k]

#2 merge_sort
# 需要开辟额外的空间来辅助归并 o(n)
def merge(alist, s, e1, e2):
	if e1 == e2:
		return 

	left = alist[s:e1+1]
	right = alist[e1+1:e2+1]

	i = 0
	j = 0
	k = s
	while True:
		if i < len(left) and j < len(right):
			if left[i] < right[j]:
				alist[k] = left[i]
				i = i + 1
			else:
				alist[k] = right[j]
				j = j + 1		
			
		elif i < len(left):
			alist[k] = left[i]
			i = i + 1
		elif j < len(right):
			alist[k] = right[j]
			j = j + 1
		else:
			break
		k = k + 1


def merge_sort(alist, start, end):
	if start < end :
		q = (start + end) // 2
		if start < q:
			merge_sort(alist, start, q)
		if q + 1 < end:
			merge_sort(alist, q + 1, end)
		merge(alist, start, q, end)

def merge_sort_no(alist, start, end):
	step = 2
	while step < len(alist):
		s = start
		for i in range(s, len(alist), step):
			




if __name__ == '__main__':
	#test_sort(insert_sort)
	#test_sort(merge_sort_no)
	for i in range(0, 10):
		print(i)


