#将图像转化为测试数据
def img2vector(filename):
	#创建要返回的1*1024的矩阵并初始化为0  
	returnVect = zeros((1,1024))
	# 打开文件  
	fr = open(filename)
	#从0到31行遍历 
	for i in range(32):
		#读取一行（自动成为一个列表）
		lineStr = fr.readline()
		#从0到31列 
		for j in range(32):
			#将一行中的每个元素复制到要返回的矩阵中  
			returnVect[0,32*i+j] = int(lineStr[j])
	#返回该1*1024的矩阵 
	return returnVect
