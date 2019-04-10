# 朴素贝叶斯分类器训练函数
# 详细解释 https://blog.csdn.net/weixin_33738982/article/details/85972316

# 输入参数是文档矩阵trainMatrix，以及每篇文档类别标签所构成的向量trainCategory
def trainNB0(trainMatrix, trainCategory):
    # 取得词向量矩阵的长度，也就是说文档的数量，此例中是6个。
    numTrainDocs = len(trainMatrix)
    # 取得词向量矩阵中第一条记录的长度，也就是词条（即特征）的数量，此例应当是32个。
    numWords = len(trainMatrix[0])
    # 通过类别i中文档数除以总的文档树计算概率p(c)
    pAbusive = sum(trainCategory) / float(numTrainDocs)
    # 初始化概率
    p0Num = zeros(numWords)
    p1Num = zeros(numWords)
    p0Denom = 0.0
    p1Denom = 0.0
    for i in range(numTrainDocs):
        # 如果文档类别是侮辱性（trainCategory[i] == 1），则把侮辱性文档的词向量相叠加，否则把非侮辱性文档的词向量相叠加
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = p1Num / p1Denom
    p0Vect = p0Num / p0Denom
    return p0Vect, p1Vect, pAbusive
