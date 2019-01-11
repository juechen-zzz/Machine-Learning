#将文本记录转换为Numpy的解析程序
def file2matrix(filename):
	fr = open(filename)
	#一次读取整个文本数据，并且自动将文件内容分析成一个行的列表，比readline（）快 ，后面的img2vector就是使用的readline（）
	arrayOLines = fr.readlines()
	numberOfLines = len(arrayOLines)
	#文件有几行就是几行，设置为3列（可调）
	returnMat = zeros((numberOfLines,3))						
	classLabelVector = []
	index = 0
	for line in arrayOLines:
		#去掉回车符,pre（使上下的数据紧凑在一起）
		line = line.strip()	
		#用‘\t’作为分隔符将整行元素分割成元素列表，按空进行分割									
		listFromLine = line.split('\t')	
		#前3个列表元素是特征，取出来去填充returnMat  						
		returnMat[index,:] = listFromLine[0:3]
		#是1 or 2 or 3，填入得到分类标签向量
		classLabelVector.append(int(listFromLine[-1]))	
		#继续迭代 		
		index +=1	
	return returnMat,classLabelVector
