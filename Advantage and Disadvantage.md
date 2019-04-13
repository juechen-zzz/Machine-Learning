# 各种算法优缺点

## 1. K-近邻算法

* 优点：精度高，对异常值不敏感，无数据输入假定
* 缺点：计算复杂度高，空间复杂度高
* 适用数据范围：数值型、标称型
* 一般流程：
  * 收集数据：任何方法
  * 准备数据：距离计算所需要的数值，最好是结构化的数据形式
  * 分析数据：任何方法
  * 训练算法：此步骤不适用与K-近邻算法
  * 测试数据：计算错误率
  * 使用算法：首先需要输入样本数据和结构化的输出结果，然后运行K-近邻算法判定输入数据属于哪个分类，最后应用对计算出的分类执行后续的处理



## 2. 决策树

* 优点：计算复杂度不高，输出结果易于理解，对中间值的缺失不敏感，可以处理不相关特征数据
* 缺点：可能会产生过度匹配问题
* 适用数据类型：数值型、标称型
* 一般流程：
  * 收集数据：任何方法
  * 准备数据：树构造算法只适用于标称型数据，因此数值型数据必须离散化
  * 分析数据：任何方法，构造完之后，应该检查图形是否符合预期
  * 训练算法：构造树的数据结构
  * 测试算法：使用经验树计算错误率
  * 使用算法：此步骤可以适用于任何监督学习算法，而使用决策树可以更好的理解数据的内在含义



## 3. 朴素贝叶斯

* 优点：在数据较少的情况下依旧有效，可以处理多类别问题
* 缺点：对于输入数据的准备方式比较敏感
* 适用数据类型：标称型数据
* 一般流程：
  * 收集数据：任何方法
  * 准备数据：需要数值型或者布尔型数据
  * 分析数据：有大量特征时，绘制特征作用不大，此时使用直方图效果更好
  * 训练算法：计算不同的独立特征的条件概率
  * 测试算法：计算错误率
  * 使用算法：一个常见的朴素贝叶斯应用是文档分类。可以在任意的分类场景中使用朴素贝叶斯分类器，不一定非要是文本。



## 4. Logistic回归

* 优点：计算代价不高，易于理解和实现
* 缺点：容易欠拟合，分类精度不高
* 适用数据类型：数值型和标称型数据
* 一般流程：
  * 收集数据：任何方法
  * 准备数据：因为要进行距离计算，要求数据类型为数值型。另外，结构化数据格式则最佳
  * 分析数据：任意方法
  * 训练算法：大部分时间用于训练，训练的目的是为了找到最佳的分类回归系数
  * 测试算法：一旦训练步骤完成，分类将会很快
  * 使用算法：首先，需要输入一些数据，并将其转换成对应的结构化数值；接着，基于训练好的回归系数就可以对这些数值进行简单的回归计算，判定它们属于哪个类别；最后，在输出的类别上做一些其他分析工作。