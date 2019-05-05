# 回归树剪枝函数

# 测试输入变量是否为一棵树
def isTree(obj):
    return (type(obj).__name__ == 'dict')

# 递归函数，从上往下遍历树，若找到两个叶节点则返回平均值
def getMean(tree):
    if isTree(tree['right']):
        tree['right'] = getMean(tree['right'])
    if isTree(tree['left']):
        tree['left'] = getMean(tree['left'])
    return (tree['left'] + tree['right']) / 2.0

# 两个参数，待剪枝的树和剪枝所需的测试数据
def prune(tree, testData):
    # 验证测试集是否为空
    if shape(testData)[0] == 0:
        return getMean(tree)
    if (isTree(tree['right']) or isTree(tree['left'])):
        lSet, rSet = binSplitDataSet(testData, tree['spInd'], tree['spVal'])
    # 左子树
    if isTree(tree['left']):
        tree['left'] = prune(tree['left'], lSet)
    # 右子树
    if isTree(tree['right']):
        tree['right'] = prune(tree['right'], rSet)
    # 检测是否仍是子树
    if not isTree(tree['left']) and not isTree(tree['right']):
        lSet, rSet = binSplitDataSet(testData, tree['spInd'], tree['spVal'])
        errorNoMerge = sum(power(lSet[:, -1] - tree['left'], 2)) + sum(power(rSet[:, -1] - tree['right'], 2))
        treeMean = (tree['left'] + tree['right']) / 2.0
        errorMerge = sum(power(testData[:, -1] - treeMean, 2))
        if errorMerge < errorNoMerge:
            print('merging')
            return treeMean
        else:
            return tree
    else:
        return tree
