# SMO算法中的辅助函数

# 打开文件并对其进行逐行解析，得到每行的类标签和整个数据矩阵
def loadDataSet(fileName):
    dataMat = []
    labelMat =[]
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = line.strip().split('\t')
        dataMat.append([float(lineArr[0]), float(lineArr[1])])
        labelMat.append(float(lineArr[2]))
    return dataMat, labelMat

# i是第一个alpha的下标,m是所有alpha的数目
def selectJrand(i, m):
    j = i
    # 只要函数值不等于输入值i，函数就会进行随机选择
    while j == i:
        j = int(random.uniform(0, m))
    return j

# 用于调整大于H或小于L的alpha值
def clipAlpha(aj, H, L):
    if aj > H:
        aj = H
    if L > aj:
        aj = L
    return aj

