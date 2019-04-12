# 朴素贝叶斯分类函数

# vec2Classify--待分类的词条数组; p0Vec--侮辱类的条件概率数组; p1Vec--非侮辱类的条件概率数组; pClass1--文档属于侮辱类的概率
def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)
    p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)
    if p1 > p0:
        return 1
    else:
        return 0

def testingNB():
    listOPosts, listClasses = loadDataSet()
    myVocabList = createVocabList(listOPosts)
    trainMat = []
    for postinDoc in listOPosts:
        # 将实验样本向量化
        trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
    # 训练朴素贝叶斯分类器
    p0V, p1V, pAb = trainNB0(array(trainMat), array(listClasses))
    # 测试样本1
    testEntry = ['love', 'my', 'dalmation']
    # 测试样本向量化
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print(testEntry, "classified as:", classifyNB(thisDoc, p0V, p1V, pAb))

    testEntry = ['stupid', 'garbage']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print(testEntry, 'classified as:', classifyNB(thisDoc, p0V, p1V, pAb))

