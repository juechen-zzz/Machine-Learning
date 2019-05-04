# CART算法的实现代码
from numpy import *

# 读取文件，将每行的内容保存成一组浮点数
def loadDataSet(fileName):
    dataMat = []
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        # 将每行映射成浮点数
        fltLine = list(map(float, curLine))
        dataMat.append(fltLine)
    return dataMat

# 3个参数：输入数据集，待切分的特征，该特征的某个值
# 通过数组过滤方式将数据集切分得到两个子集
def binSplitDataSet(dataSet, feature, value):
    mat0 = dataSet[nonzero(dataSet[:, feature] > value)[0], :]
    mat1 = dataSet[nonzero(dataSet[:, feature] <= value)[0], :]
    return mat0, mat1

# 树构建函数，递归函数
# leafType是对创建叶节点的函数的引用
# errType是对总方差计算函数的引用
# ops是一个用户定义的参数的元组
def createTree(dataSet, leafType = regLeaf, errType = regErr, ops = (1, 4)):
    feat, val = chooseBestSplit(dataSet, leafType, errType, ops)
    # 若满足停止条件，将返回None和某类模型的值
    if fear == None:
        return val
    retTree = {}
    retTree['spInd'] = feat
    retTree['spVal'] = val
    lSet, rSet = binSplitDataSet(dataSet, feat, val)
    retTree['left'] = createTree(lSet, leafType, errType, ops)
    retTree['right'] = createTree(rSet, leafType, errType, ops)
    return retTree
