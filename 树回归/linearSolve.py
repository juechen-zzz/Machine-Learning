# 模型树的叶节点生成函数

# 将数据集格式化为目标变量Y和自变量X
def linearSolve(dataSet):
    m, n = shape(dataSet)
    X = mat(ones((m, n)))
    Y = mat(ones((m, 1)))
    X[:, 1:n] = dataSet[:, 0:n-1]
    Y = dataSet[:, -1]
    xTx = X.T * X
    if linalg.det(xTx) == 0.0:
        raise NameError('this matrix is singular, can not do inverse,\n try increasing the second value of ops')
    ws = xTx.I * (X.T * Y)
    return ws, X, Y

# 当数据不再需要切分的时候负责生成叶节点的模型
def modelLeaf(dataSet):
    ws, X, Y = linearSolve(dataSet)
    return ws

# 在给定的数据集上计算误差
def modelErr(dataSet):
    ws, X, Y = linearSolve(dataSet)
    yHat = X * ws
    return sum(power(Y - yHat, 2))