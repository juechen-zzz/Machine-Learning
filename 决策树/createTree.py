# 创建树的函数代码

def createTree(dataSet, labels):
    # 类别标签列表
    classList = [example[-1] for example in dataSet]
    # 类别完全相同则停止继续划分
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    # 遍历完所有特征时返回出现次数最多的类别
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)
    # 获得最佳特征的下标和名称
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    # 以最佳特征为根节点创建子树
    myTree = {bestFeatLabel: {}}
    # 在特征名列表中删除最佳特征(创建节点需要消耗特征)
    del (labels[bestFeat])
    # 获得最佳特征的所有可能值
    featValues = [example[bestFeat] for example in dataSet]
    # 去除重复的值
    uniqueVals = set(featValues)
    # 遍历当前选择特征包含的所有属性值
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)
    return myTree
