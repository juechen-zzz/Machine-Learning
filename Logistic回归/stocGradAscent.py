# 随机梯度上升算法
def stocGradAscent0(dataMatrix, classLabels):
    # m为行 n为列
    m, n = shape(dataMatrix)
    alpha = 0.01
    weights = ones(n)
    for i in range(m):
        h = sigmoid(sum(dataMatrix[i] * weights))
        error = classLabels[i] - h
        weights = weights + alpha * error * dataMatrix[i]
    return weights

# 改进的随机梯度上升算法
def stocGradAscent1(dataMatrix, classLabels, numIter=150):
    m, n = shape(dataMatrix)
    weights = ones(n)
    # 随机梯度, 循环150,观察是否收敛
    for j in range(numIter):
        dataIndex = range(m)
        for i in range(m):
            # alpha会随着迭代次数不断减小，但不会是0
            alpha = 4 / (1.0 + j + i) + 0.01
            # random.uniform(x, y) 方法将随机生成下一个实数，它在[x,y]范围内,x是这个范围内的最小值，y是这个范围内的最大值。
            randIndex = int(random.uniform(0, len(dataIndex)))
            # 随机选取更新
            h = sigmoid(sum(dataMatrix[randIndex] * weights))
            error = classLabels[randIndex] - h
            weights = weights + alpha * error * dataMatrix[randIndex]
            del(dataIndex[randIndex])
    return weights
