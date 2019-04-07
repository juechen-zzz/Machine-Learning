# 选择最好的数据集划分方式

# 2个要求，第一，数据必须是一种列表元素组成的列表，且所有元素等长；第二，数据的最后一列或者每个实例的最后一个元素是类比标签。

def chooseBestFeatureToSplit(dataSet):
    # 判定当前数据集包含多少特征属性
    numFeatures = len(dataSet[0]) - 1
    # 计算原始香农熵，设定最初的无序度量值
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1
    # 遍历数据集中的所有特征
    for i in range(numFeatures):
        # 创建唯一的分类标签列表，使用列表推导（list comprehension)来创建新的列表，将数据集中所有第i个特征值写入这个list中。
        featList = [example[i] for example in dataSet]
        # 从列表中创建集合是python语言中得到列表中唯一元素值的最快方法
        uniqueVals = set(featList)
        newEntropy = 0.0
        # 遍历当前特征的所有唯一属性值，对每个唯一属性值划分一次数据集，并计算熵值及求和。
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet) / float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy
        # 计算最好的信息增益，返回最好特征划分的索引值。
        if infoGain > bestInfoGain:
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature
