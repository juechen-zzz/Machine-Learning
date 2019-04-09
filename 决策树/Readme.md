# Code structure

* trees.py is the main algorithm. The rest of the file is an understanding of each function.
* treePlotter.py is using Matplotlib to draw a treemap.
* Prediction of contact lens type renderings through decision trees.



```python
fr = open('lenses.txt')
lenses = [inst.strip().split('\t') for inst in fr.readlines()]
lensesLabels = ['age', 'prescript', 'astigmatic', 'tearRate']
lensesTree = trees.createTree(lenses,lensesLabels)
treePlotter.createPlot(lensesTree)
```

