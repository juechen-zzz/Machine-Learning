# Code structure

* trees.py is the main algorithm. The rest of the file is an understanding of each function.
* treePlotter.py is using Matplotlib to draw a treemap.
* Prediction of contact lens type renderings through decision trees.

![image](https://github.com/juechen-zzz/Machine-Learning/blob/master/%E5%86%B3%E7%AD%96%E6%A0%91/Rendering.jpg)

```python
fr = open('lenses.txt')
lenses = [inst.strip().split('\t') for inst in fr.readlines()]
lensesLabels = ['age', 'prescript', 'astigmatic', 'tearRate']
lensesTree = trees.createTree(lenses,lensesLabels)
treePlotter.createPlot(lensesTree)
```

