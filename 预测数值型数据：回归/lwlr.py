# 局部加权线性回归函数
def lwlr(testPoint, xArr, yArr, k = 1.0):
    # 读入数据创建所需矩阵
    xMat = mat(xArr)
    yMat = mat(yArr).T
    m = shape(xMat)[0]
    # 创建对角权重矩阵，是一个方阵，阶数等于样本点数
    weights = mat(eye((m)))
    # 遍历，用核函数衰减权重
    for j in range(m):
        diffMat = testPoint - xMat[j, :]
        weights[j, j] = exp(diffMat * diffMat.T / (-2.0 * k ** 2))
    xTx = xMat.T * (weights * xMat)
    if linalg.det(xTx) == 0.0:
        print('this matrix is singular, can not do inverse')
        return
    ws = xTx.I * (xMat.T * (weights * yMat))
    return testPoint * ws

# 用于为数据集中每个点调用lwlr()，有助于求解k
def lwlrTest(testArr, xArr, yArr, k=1.0):
    m = shape(testArr)[0]
    yHat = zeros(m)
    for i in range(m):
        yHat[i] = lwlr(testArr[i], xArr, yArr, k)
    return yHat

def rssError(yArr, yHatArr):
    return ((yArr - yHatArr) ** 2).sum()
