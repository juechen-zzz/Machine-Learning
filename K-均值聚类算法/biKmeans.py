# 二分K-均值聚类算法

def biKmeans(dataSet, k, distMeas = distEclud):
    # 行数，数据集中点的个数
    m = shape(dataSet)[0]
    # 创建一个初试簇，存储每个点的簇分配结果及平方误差，然后计算整个数据集的质心
    clusterAssment = mat(zeros((m, 2)))
    centroid0 = mean(dataSet, axis=0).tolist()[0]
    centList = [centroid0]
    for j in range(m):
        clusterAssment[j, 1] = distMeas(mat(centroid0), dataSet[j, :])**2
    # 不停的对簇进行划分，直到得到想要的簇数目为止
    while len(centList) < k:
        # 初始sse设置为无穷
        lowestSSE = inf
        # 遍历所有簇，将每个簇中的所有点看成是一个小的数据集，再生出2个质心的簇，同时给出误差
        for i in range(len(centList)):
            ptsInCurrCluster = dataSet[nonzero(clusterAssment[:, 0].A == i)[0], :]
            centroidMat, splitClustAss = kMeans(ptsInCurrCluster, 2, distMeas)
            sseSplit = sum(splitClustAss[:, 1])
            sseNotSplit = sum(clusterAssment[nonzero(clusterAssment[:, 0].A != i)[0], 1])
            print('sseSplit, and nonSplit:', sseSplit, sseNotSplit)
            if (sseSplit + sseNotSplit) < lowestSSE:
                bestCentToSplit = i
                bestNewCents = centroidMat
                bestClustAss = splitClustAss.copy()
                lowestSSE = sseSplit + sseNotSplit
        # 更新簇的分配结果
        bestClustAss[nonzero(bestClustAss[:, 0].A == 1)[0], 0] = len(centList)
        bestClustAss[nonzero(bestClustAss[:, 0].A == 0)[0], 0] = bestCentToSplit
        print('the bestCentToSplit is:',bestCentToSplit)
        print('the len of bestClustAss is :', len(bestClustAss))
        centList[bestCentToSplit] = bestNewCents[0, :]
        centList.append(bestNewCents[1, :])
        clusterAssment[nonzero(clusterAssment[:,0].A == bestCentToSplit)[0], :] = bestClustAss
        return centList, clusterAssment
