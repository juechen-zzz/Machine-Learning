# 基于单层决策树的AdaBoost训练过程

# 输入参数：数据集，类别标签，迭代次数，DS代表单层决策树
def adaBoostTrainDS(dataArr, classLabels, numIt = 40):
    weakClassArr = []
    m = shape(dataArr)[0]
    # D包含了每个数据点的权重，一开始赋值为1/m
    D = mat(ones((m, 1)) / m)
    # 列向量，记录每个数据点的类别估计累计值
    aggClassEst = mat(zeros((m, 1)))
    for i in range(numIt):
        # 首先，建立一个单层决策树，返回最优单层决策树、最小的错误率、估计的类别向量
        bestStump, error, classEst = buildStump(dataArr, classLabels, D)
        print('D:', D.T)
        # 告诉总分类器本次单层决策树输出结果的权重，并确保不会发生除零移除
        alpha = float(0.5 * log((1.0 - error) / max(error, 1e-16)))
        bestStump['alpha'] = alpha
        weakClassArr.append(bestStump)
        print('classEst:', classEst.T)
        # 计算下一次迭代中的新权重向量D
        expon = multiply(-1 * alpha * mat(classLabels).T, classEst)
        D = multiply(D, exp(expon))
        D = D / D.sum()
        # 错误率累加计算
        aggClassEst += alpha * classEst
        print('aggClassEst:', aggClassEst.T)
        aggErrors = multiply(sign(aggClassEst) != mat(classLabels).T, ones((m, 1)))
        errorRate = aggErrors.sum() / m
        print('total error:', errorRate, '\n')
        # 若迭代后错误率为0，则退出迭代过程
        if errorRate == 0:
            break
    return weakClassArr
