# 检测是否出现了词汇表中的单词
def setOfWords2Vec(vocabList, inputSet):
    # 创建一个其中所含元素都为0的向量，和词汇表等长
    returnVec = [0] * len(vocabList)
    # 遍历整个文档中的单词，若出现词汇表中的词，则输出值为1，否则为0
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else:
            print('the word: %s is not in my vocabulary', word)
    return returnVec
