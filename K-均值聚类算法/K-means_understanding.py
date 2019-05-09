# K-均值聚类算法

# 四个参数：数据集，质心数，距离函数，创建质心函数
def kMeans(dataSet, k, distMeas = distEclud, createCent = randCent):
    # 行数，确定数据集中数据点的总数
    m = shape(dataSet)[0]
    # 创建一个矩阵存储每个点的簇分配结果
    clusterAssment = mat(zeros((m, 2)))
    # 调用函数生成随机质心
    centroids = createCent(dataSet, k)
    # 创建一个标志变量，若为true，则继续迭代
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        # 寻找最近的质心
        for i in range(m):
            minDist = inf
            minIndex = -1
            for j in range(k):
                distJI = distMeas(centroids[j, :], dataSet[i, :])
                if distJI < minDist:
                    minDist = distJI
                    minIndex = j
            if clusterAssment[i, 0 ] != minIndex:
                clusterChanged = True
            clusterAssment[i, :] = minIndex, minDist**2
        print(centroids)
        # 更新质心的位置
        for cent in range(k):
            ptsInClust = dataSet[nonzero(clusterAssment[:, 0].A == cent)[0]]
            centroids[cent, :] = mean(ptsInClust, axis = 0)
    return centroids, clusterAssment
