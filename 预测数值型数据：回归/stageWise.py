# 正则化
def regularize(xMat):
    inMat = xMat.copy()
    inMeans = mean(inMat,0)
    inVar = var(inMat,0)
    inMat = (inMat - inMeans)/inVar
    return inMat

# 前向逐步线性回归
def stageWise(xArr, yArr, eps=0.01, numIt=100):
    # 数据标准化，使其满足0均值和单位方差
    xMat = mat(xArr)
    yMat = mat(yArr).T
    yMean = mean(yMat, 0)
    yMat = yMat - yMean
    xMat = regularize(xMat)
    m, n = shape(xMat)
    returnMat = zeros((numIt, n))
    ws = zeros((n, 1))
    wsTest = ws.copy()
    wsMax = ws.copy()
    for i in range(numIt):
        print(ws.T)
        # 设置当前最小误差为正无穷
        lowestError = inf
        for j in range(n):
            # 两次循环，计算增加或者减少该特征对误差的影响
            for sign in [-1, 1]:
                wsTest = ws.copy()
                wsTest[j] += eps * sign
                yTest = xMat * wsTest
                rssE = rssError(yMat.A, yTest.A)
                if rssE < lowestError:
                    lowestError = rssE
                    wsMax = wsTest
        ws = wsMax.copy()
        returnMat[i, :] = ws.T
    return returnMat

