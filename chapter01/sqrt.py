'''
计算某个数的开放值为多少
'''
def getSqrt(num,ans=0.01):
	'''
	num:想要开根的数
	ans:精度
	'''
	step = ans ** 2
	base = 0.03
	geussNum = 0
	while abs(base**2 - num) >= ans and base <= num:
		base += step
		geussNum += 1
	return base,geussNum
print(getSqrt(25))