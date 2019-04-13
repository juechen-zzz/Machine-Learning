# Code structure

* logRegres.py is the main algorithm. The rest of the file is an understanding of each function.
* logRegres.py is using Matplotlib to draw a figure.

```python
import logRegres
dataArr,labelMat = logRegres.loadDataSet()
weights = logRegres.gradAscent(dataArr,labelMat)
logRegres.plotBestFit(weights.getA())
```

