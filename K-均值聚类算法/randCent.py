# K-均值聚类支持函数
def loadDataSet(fileName):
    dataMat = []
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        fltLine = list(map(float,curLine))
        dataMat.append(fltLine)
    return dataMat

# 计算欧几里德距离
def distEclud(vecA, vecB):
    return sqrt(sum(power(vecA - vecB, 2)))

# 生成随机中心质点,k个随机质心
def randCent(dataSet, k):
    n = shape(dataSet)[1]
    centroids = mat(zeros((k,n)))
    # 构建簇质心
    for j in range(n):
        minJ = min(dataSet[:,j])
        rangeJ =float(max(dataSet[:, j]) - minJ)
        # random.rand生成k行1列的数组，其中元素值均分布在（0，1）范围内，实际上是每列对应向量的计算
        centroids[:,j] = minJ + rangeJ * random.rand(k, 1)
    return centroids