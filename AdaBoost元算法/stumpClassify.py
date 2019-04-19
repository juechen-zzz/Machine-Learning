# 单层决策树生成函数

# 参数：输入序列，第几列，阈值， lt或gt
# 比对每一列的特征值和目标函数，返回比对的结果
def stumpClassify(dataMatrix, dimen, threshVal, threshIneq):
    retArray = ones((shape(dataMatrix)[0], 1))
    if threshIneq == 'lt':
        retArray[dataMatrix[:, dimen] <= threshVal] = -1.0
    else:
        retArray[dataMatrix[:, dimen] > threshVal] = -1.0
    return retArray

# 构建二叉树函数，通过循环比較得到最佳特征值和它的阈值。D是初始矩阵的权重
def buildStump(dataArr, classLabels, D):
    dataMatrix = mat(dataArr)
    labelMat = mat(classLabels).T
    m, n = shape(dataMatrix)
    numSteps = 10.0
    bestStump = {}
    bestClasEst = mat(zeros((m, 1)))
    minError = inf
    # 对每个特征循环, 选择的特征是最好的
    for i in range(n):
        # rangeMin, rangeMax分别代表数据集中特征的最小和最大值
        rangeMin = dataMatrix[:, i].min()
        rangeMax = dataMatrix[:, i].max()
        # 在特征的范围内选定步长,选择最合适的阈值
        stepSize = (rangeMax - rangeMin) / numSteps
        # ‘lt’和’gt’分别代表两种情况:第一种:’lt’:低于阈值的是分类为-1的,第二种:’gt’:高于阈值的分类为-1
        for j in range(-1, int(numSteps) + 1):
            for inequal in ['lt', 'gt']:
                threshVal = (rangeMin + float(j) * stepSize)
                predictedVals = stumpClassify(dataMatrix, i, threshVal, inequal)
                errArr = mat(ones((m, 1)))
                errArr[predictedVals == labelMat] = 0
                weightedError = D.T * errArr
                print('split : dim %d, thresh %.2f, thresh inequql : %s, the weighted error is %.3f' % (i, threshVal, inequal, weightedError))
                # 最终单层决策树的原则:minError,误差最小
                if weightedError < minError:
                    minError = weightedError
                    bestClasEst = predictedVals.copy()
                    bestStump['dim'] = i
                    bestStump['thresh'] = threshVal
                    bestStump['ineq'] = inequal
    return bestStump, minError, bestClasEst

