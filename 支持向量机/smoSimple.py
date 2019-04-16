# 简化版SMO算法

# 5个输入参数：数据集，类别标签，常数C，容错率，退出前的最大循环次数
def smoSimple(dataMatIn, classLabels, C, toler, maxIter):
    dataMatrix = mat(dataMatIn)
    labelMat = mat(classLabels).transpose()
    b = 0
    # dataMatIn的行、列
    m, n = shape(dataMatrix)
    alphas = mat(zeros((m, 1)))
    # 存储没有任何alpha改变情况下遍历数据集的次数
    iter = 0
    while iter < maxIter:
        # 记录alpha是否已经进行优化
        alphaParisChanged = 0
        for i in range(m):
            # 预测的类别
            fXi = float(multiply(alphas, labelMat).T * (dataMatrix * dataMatrix[i, :].T)) + b
            # 步骤1，计算误差
            Ei = fXi - float(labelMat[i])
            # 误差过大则进行alpha优化
            if (labelMat[i] * Ei < -toler and alphas[i] < C) or (labelMat[i] * Ei > toler and alphas[i] > 0):
                j = selectJrand(i, m)
                fXj = float(multiply(alphas, labelMat).T * (dataMatrix * dataMatrix[j, :].T)) + b
                Ej = fXj - float(labelMat[j])
                alphaIold = alphas[i].copy()
                alphaJold = alphas[j].copy()
                # 步骤2，对alpha_2_new进行裁剪的上下界 (L,H)
                if labelMat[i] != labelMat[j]:
                    L = max(0, alphas[j] - alphas[i])
                    H = min(C, C + alphas[j] - alphas[i])
                else:
                    L = max(0, alphas[j] + alphas[i] - C)
                    H = min(C, alphas[j] + alphas[i])
                if L == H:
                    print('L == H')
                    continue
                # 步骤3，计算eta
                eta = 2.0 * dataMatrix[i, :] * dataMatrix[j, :].T - dataMatrix[i, :] * dataMatrix[i, :].T \
                      - dataMatrix[j, :] * dataMatrix[j, :].T
                if eta >= 0 :
                    print('eta >=0')
                    continue
                # 步骤4，更新alphas[j]
                alphas[j] -= labelMat[j] * (Ei - Ej) / eta
                # 步骤5，修建alphas[j]
                alphas[j] = clipAlpha(alphas[j], H, L)
                if abs(alphas[j] - alphaJold) < 0.00001:
                    print('j not moving enough')
                    continue
                # 步骤6，更新alphas[i]
                alphas[i] += labelMat[j] * labelMat[i] * (alphaJold - alphas[j])
                # 步骤7，更新b1,b2
                b1 = b - Ei - labelMat[i] * (alphas[i] - alphaIold) * dataMatrix[i, :] * dataMatrix[i, :].T \
                     - labelMat[j] * (alphas[j] - alphaJold) * dataMatrix[i, :] * dataMatrix[j, :].T
                b2 = b - Ej - labelMat[i] * (alphas[i] - alphaIold) * dataMatrix[i, :] * dataMatrix[j, :].T \
                     - labelMat[j] * (alphas[j] - alphaJold) * dataMatrix[j, :] * dataMatrix[j, :].T
                # 步骤8，更新b
                if 0 < alphas[i] and C > alphas[i]:
                    b = b1
                elif 0 < alphas[j] and C > alphas[j]:
                    b = b2
                else:
                    b = (b1 + b2) / 2.0
                alphaParisChanged += 1
                print('iter: %d i :%d, pairs changed %d' % (iter, i, alphaParisChanged))
        if alphaParisChanged ==0:
            iter += 1
        else:
            iter = 0
        print('iteration number : %d' % iter)
    return b, alphas


