# 划分数据集

# 3个输入参数：带划分的数据集，划分数据集的特征，需要返回的特征的值
def splitDataSet(dataSet, axis, value):
    # 创建新的列表对象，因为被调用多次，为不改变原始数据集
    retDataSet = []
    # 遍历数据集中的每个元素，一旦发现符合要求的值，就添加到新创建的列表中
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis + 1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet
