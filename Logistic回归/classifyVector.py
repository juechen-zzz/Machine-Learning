# Logistics回归分类函数

# 以回归系数和特征向量作为输入计算sigmoid值
def classifyVector(inX, weights):
    prob = sigmoid(sum(inX * weights))
    if prob > 0.5 :
        return 1.0
    else:
        return 0.0

def colicTest():
    # 打开训练和测试集
    frTrain = open('horseColicTraining.txt')
    frTest = open('horseColicTest.txt')
    trainingSet = []
    trainingLabels = []
    # 训练
    for line in frTrain.readlines():
        currLine = line.strip().split('\t')
        lineArr = []
        for i in range(21):
            lineArr.append(float(currLine[i]))
        trainingSet.append(lineArr)
        trainingLabels.append(float(currLine[21]))
    trainWeights = stocGradAscent1(array(trainingSet), trainingLabels, 500)
    errorCount = 0
    numTestVec = 0.0
    # 测试
    for line in frTest.readlines():
        numTestVec += 1.0
        currLine = line.strip().split('\t')
        lineArr = []
        for i in range(21):
            lineArr.append(float(currLine[i]))
        if int(classifyVector(array(lineArr), trainWeights)) != int(currLine[21]):
            errorCount += 1
    # 计算错误率
    errorRate = (float(errorCount) / numTestVec)
    print('the error rate of this test is :', errorRate)
    return errorRate

# 调用colicTest()10次并求结果的平均值
def multiTest():
    numTests = 10
    errorSum = 0.0
    for k in range(numTests):
        errorSum += colicTest()
    print('after %d iterations the average error rate is : %f' % (numTests, errorSum / float(numTests)))

