#测试代码
def datingClassTest():
	#测试所占的比例 
	hoRatio = 0.10
	#将文件中的数据转换为矩阵形式和提取出标签矩阵  
	datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')
	#对提取出的矩阵数据归一化处理 
	normMat,ranges,minVals = autoNorm(datingDataMat)
	#获得数据总的条数  
	m = normMat.shape[0]
	#得出作为测试的数据个数  
	numTestVecs = int(m * hoRatio)

	errorCount = 0.0

	#对测试的数据进行遍历
	for i in range(numTestVecs):
		# 对数据进行分类 
		classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],3)
		#输出分类结果和实际的类别(之前的代码有问题啊，要将%d,改为%s)  
		print("the classifier came back with : %d, the real answer is : %d" % (classifierResult,datingLabels[i]))
		if classifierResult != datingLabels[i]:
			errorCount += 1.0
	print("the total error rate is : %f" % (errorCount/float(numTestVecs)))
	print(errorCount)    #输出错误总数