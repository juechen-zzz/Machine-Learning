#计算给定数据集的香农熵
from math import log

def calcShannonEnt(dataSet):
	#计算样本总数
	numEntries = len(dataSet)
	#创建数据字典，其键值是最后一列的数值
	labelCounts = {}
	#定义特征向量featVec
	for featVec in dataSet:
		#最后一列是类别标签
		currentLabel = featVec[-1]
		#如果当前键值不存在，则扩展字典并将当前键值加入字典
		if currentLabel not in labelCounts.keys():
			labelCounts[currentLabel] = 0
		#每一个键值都记录了当前类别的次数
		labelCounts[currentLabel] += 1
	shannonEnt = 0.0
	for key in labelCounts:
		#每一个类别标签出现的概率
		prob = float(labelCounts[key]) / numEntries
		#求熵值
		shannonEnt -= prob*log(prob,2)
	return shannonEnt