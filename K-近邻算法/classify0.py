#程序2-1

def classify0(inX, dataSet, labels, k):
    # inX为待分类数据
    # dataSet为训练数据集
    # labels对应dataSet每一行数据的标签(类型)

    # 有多少行数据 shape反回一个元组。(行, 列)
    dataSetSize = dataSet.shape[0] 
    
    # tile(inX, (dataSetSize,1)) 创建一个numpy的array，dataSetSize行1列，每行数据是inX
    diffMat = tile(inX, (dataSetSize,1)) - dataSet 
    
    # 矩阵的每个值平方
    sqDiffMat = diffMat**2

    # 横向求和，得到一个一维数组，每个值都是和
    sqDistances = sqDiffMat.sum(axis=1)
    
    # 数组中每个值开根
    distances = sqDistances**0.5

    # 得到排序后的下标数组
    sortedDistIndicies = distances.argsort()

    classCount={}
    # 只取前k个        
    for i in range(k):
        # 找到下标对应的标签
        voteIlabel = labels[sortedDistIndicies[i]]
        # classCount.get(voteIlabel,0)返回字典classCount中voteIlabel元素对应的值,若无，则进行初始化
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    # 排序加反转
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    print sortedClassCount
    # 把计数最大的值所对应的标签返回出去
    return sortedClassCount[0][0]
