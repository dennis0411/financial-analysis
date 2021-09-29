from sklearn import tree
from sklearn import datasets
from sklearn.model_selection import train_test_split
import pydotplus
import pandas as pd


iris = datasets.load_iris() # 資料為 dictionary array,可用pandas針對字典內容重新整理
X = iris.data
y = iris.target

#全樣本種樹
# clf = tree.DecisionTreeClassifier(criterion='entropy').fit(X,y)
# clf.score(X, y)


#看看種了什麼樹
#另外安裝 GraphViz's 參考網址 https://blog.csdn.net/qq_40304090/article/details/88594813

# dot_data = tree.export_graphviz(clf, out_file=None)
# graph = pydotplus.graph_from_dot_data(dot_data)
# graph.write_pdf('iris.pdf')


#分樣本訓練種樹
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
# clf = tree.DecisionTreeClassifier(criterion='entropy').fit(X_train, y_train)
# x = clf.predict(X_test)
# print('測試分數 :', clf.score(X_test, y_test))
# print('預測結果 :', x) #再利用 pd 還原

#調整種樹方向1 : 限制三層樹
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3) #實作上加入 random_state=42 固定結果
clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=3).fit(X_train, y_train)
x = clf.predict(X_test)
print('測試分數 :', clf.score(X_test, y_test))
print('預測結果 :', x) #再利用 pd 還原