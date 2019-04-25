# 导入数据
def loadDataSet(fileName):
    # 读取文件
    numFeat = len(open(fileName).readline().split('\t')) - 1
    dataMat = []
    labelMat = []
    fr = open(fileName)
    # 遍历存储
    for line in fr.readlines():
        lineArr = []
        curLine = line.strip().split('\t')
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return dataMat, labelMat

# 标准回归函数
def standRegres(xArr, yArr):
    xMat = mat(xArr)
    yMat = mat(yArr).T
    xTx = xMat.T * xMat
    # 判断是否可逆，linalg.det()用于计算行列式
    if linalg.det(xTx) == 0.0:
        print('this matrix is singular, can not do inverse')
        return
    # 标准ws的公式
    ws = xTx.I * (xMat.T * yMat)
    return ws

