# Code structure

* logRegres.py is the main algorithm. The rest of the file is an understanding of each function.
* logRegres.py is using Matplotlib to draw a figure.
* https://github.com/juechen-zzz/Machine-Learning/blob/master/Logistic%E5%9B%9E%E5%BD%92/Figure_1.png

```python
import logRegres
dataArr,labelMat = logRegres.loadDataSet()
weights = logRegres.gradAscent(dataArr,labelMat)
logRegres.plotBestFit(weights.getA())
```

