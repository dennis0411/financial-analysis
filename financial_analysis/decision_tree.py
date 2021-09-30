from sklearn import tree
from financial_analysis import data
import pydotplus


# 全樣本種樹
# clf = tree.DecisionTreeClassifier(criterion='entropy').fit(data.X,data.y)
# clf.score(data.X, data.y)

# 調整種樹方向1 : 限制三層樹
clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=3).fit(data.X_train, data.y_train)
y_predict = clf.predict(data.X_test)
print('測試分數 :', clf.score(data.X_test, data.y_test))
print('預測結果 :', y_predict)  # 再利用 pd 還原


# 看看種了什麼樹
# 另外安裝 GraphViz's 參考網址 https://blog.csdn.net/qq_40304090/article/details/88594813
dot_data = tree.export_graphviz(clf, out_file=None)
graph = pydotplus.graph_from_dot_data(dot_data)
# graph.write_pdf('iris.pdf') #pdf輸出到資料夾
