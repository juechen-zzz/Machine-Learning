# 岭回归

# 用于计算回归系数
def ridgeRegres(xMat, yMat, lam=0.2):
    xTx = xMat.T * xMat
    # eye实现单位矩阵
    denom = xTx + eye(shape(xMat)[1]) * lam
    if linalg.det(denom) == 0.0:
        print('this matrix is singular, can not do inverse')
        return
    # 公式，  .I代表求逆
    ws = denom.I * (xMat.T * yMat)
    return ws

def ridgeTest(xArr, yArr):
    xMat = mat(xArr)
    yMat = mat(yArr).T
    yMean = mean(yMat, 0)
    yMat = yMat - yMean
    xMearns = mean(xMat, 0)
    xVar = var(xMat, 0)
    xMat = (xMat - xMearns) / xVar
    numTestPts = 30
    wMat = zeros((numTestPts, shape(xMat)[1]))
    for i in range(numTestPts):
        ws = ridgeRegres(xMat, yMat, exp(i-10))
        wMat[i, :] = ws.T
    return wMat