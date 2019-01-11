#约会网站预测函数
def classifyPerson():
	# 定义分类结果的类别
	resultList = ['not at all','in small doses','in large doses']
	# 读取输入数据   
	percentTats = float(input("percentage of time spent playing video games?"))
	ffMiles = float(input("frequent filter miles earned per year?"))
	iceCream = float(input("liters of ice cream consumed per year?"))
	# 从文件中读取已有数据  
	datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')
	# 对数据进行归一化  
	normMat,ranges,minVals = autoNorm(datingDataMat)
	# 将单个输入数据定义成一条数据  
	inArr = array([ffMiles,percentTats,iceCream])
	# 对输入数据进行分类  
	classifierResult = classify0((inArr - minVals)/ranges,normMat,datingLabels,3)
	#输出
	print("You will probably like this person :",resultList[classifierResult - 1])

