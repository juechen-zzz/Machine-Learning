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



## 5. 支持向量机

* 优点：泛化错误率低，计算开销不大，结果易解释
* 缺点：对参数调节和核函数的选择敏感，原始分类器不加修改仅适用处理二类问题
* 适用数据类型：数值型和标称型数据
* 一般流程:
  * 收集数据：任意方法
  * 准备数据：需要数值型数据
  * 分析数据：有助于可视化分隔超平面
  * 训练算法：SVM的大部分时间都源于训练，该过程主要实现两个参数的调优
  * 测试算法：简单计算
  * 使用算法：几乎所有分类问题都可以使用SVM，SVM本身是一个二类分类器，对多类问题需要对代码做一些修改



## 6. AdaBoost元算法

* 优点：泛化错误率低，易编码，可以应用在大部分分类器上，无参数调整
* 缺点：对离群点敏感
* 适用数据类型：数值型和标称型数据
* 一般流程：
  * 收集数据：任意方法
  * 准备数据：依赖于所使用的弱分类器类型，此次使用单层决策树，这种分类器可以处理任何数据类型。1到5都可充当弱分类器，作为弱分类器，简单分类器的效果更好
  * 分析数据：任意方法
  * 训练数据：大部分时间，分类器将多次在同一数据集上训练弱分类器
  * 测试算法：计算分类的错误率
  * 使用算法：同SVM一样，AdaBoost预测两个类别中的一个，若想应用到多个类别的场合，则需要做修改

## 7. 预测数值型数据：回归

* 优点：结果易于理解，计算上不复杂
* 缺点：对非线性的数据拟合不好
* 适用数据类型：数值型和标称型数据
* 回归的一般流程：
  * 收集数据：任意方法
  * 准备数据：回归需要数值型数据，标称型数据将被转换成二值型数据
  * 分析数据：绘出数据的可视化二维图将有助于对数据做出理解和分析，在采用缩减法求得新回归系数后，可以将新拟合线绘制在图上做出对比
  * 训练算法：找到回归系数
  * 测试算法：使用R^2或者预测值和数据的拟合度，来分析模型的效果
  * 使用算法：使用回归，可以在给定输入的时候预测出一个数值，这是对分类方法的提升，因为这样可以预测连续型数据而不仅仅是离散的类别标签



## 8. 树回归

* 优点：可以对复杂和非线性的数据建模
* 缺点：结果不易理解
* 适用数据类型：数值型和标称型数据
* 树回归的一般方法：
  * 收集数据：任意方法
  * 准备数据：需要数值型的数据，标称型数据应该映射成二值型数据
  * 分析数据：绘出数据的二维可视化显示结果，以字典方式生成树
  * 训练算法：大部分时间都花费在叶节点树模型的构建上
  * 测试算法：使用测试数据上的R^2值来分析模型的效果
  * 使用算法：使用训练出的树做预测，预测结果还可以用来做很多事情



## 9. K-均值聚类算法

* 优点：易实现
* 缺点：可能收敛到局部最小值，在大规模数据上收敛较慢
* 适用数据类型：数值型数据
* 一般方法：
  * 收集数据：任意方法
  * 准备数据：需要数值型数据来计算距离，也可以将标称型数据映射为二值型数据再用于距离计算
  * 分析数据：使用任意方法
  * 训练算法：不适用于无监督学习，即无监督学习没有训练过程
  * 测试算法：应用聚类算法、观察结果。可以使用量化的误差指标如误差平方和来评价算法的结果
  * 使用算法：可以用于所希望的任何应用，通常情况下，簇质心可以代表整个簇的数据来做出决策