#使用算法识别手写数字
def handwritingClassTest():
	# 定义手写字符标签(类别)  
	hwLabels = []
	# 列出目录下所有的文件  
	trainingFileList = listdir('trainingDigits')
	# 计算训练文件的数目  
	m = len(trainingFileList)
	# 定义手写字符数据矩阵  
	trainingMat = zeros((m,1024))
	# 依次读取每个文件  
	for i in range(m):
		# 依次获得文件名   
		fileNameStr = trainingFileList[i]
		# 对文件名进行分割  
		fileStr = fileNameStr.split('.')[0]
		# 获得文件名中的类标签  
		classNumStr = int(fileStr.split('_')[0])
		# 把类标签放到hwLabels中 
		hwLabels.append(classNumStr)
		# 把文件变成向量并赋值到trainingMat这个矩阵中  
		trainingMat[i,:] = img2vector('trainingDigits/%s' % fileNameStr)
	# 列出测试目录下的所有文件
	testFileList = listdir('testDigits')
	errorCount = 0.0
	# 获得测试文件数目 
	mTest = len(testFileList)
	# 遍历测试文件 
	for i in range(mTest):
		# 定义测试文件名  
		fileNameStr = testFileList[i]
		# 对测试文件名进行分割  
		fileStr = fileNameStr.split('.')[0]
		# 获得测试文件的类标签  
		classNumStr = int(fileStr.split('_')[0])
		# 将测试文件转换成向量  
		vectorUnderTest = img2vector('testDigits/%s' % fileNameStr)
		# 进行分类   
		classifierResult = classify0(vectorUnderTest,trainingMat,hwLabels,3)
		# 输出预测类别和实际类别 
		print("the classifier came back with : %d , the real answer is : %d" % (classifierResult,classNumStr))
		if classifierResult != classNumStr :
			errorCount += 1.0
	print("\nthe total number of errors is : %d" % errorCount)
	print("\nthe total error rate is : %f" % (errorCount/float(mTest)))
