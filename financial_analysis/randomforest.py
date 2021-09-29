from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
from financial_analysis import data


rfc = RandomForestClassifier(n_estimators=100, n_jobs=-1, random_state=50, min_samples_leaf=10)
rfc.fit(data.X_train, data.y_train)
y_predict = rfc.predict(data.X_test)
print('測試分數 :', rfc.score(data.X_test, data.y_test))
print('預測結果 :', y_predict)  # 再利用 pd 還原

#Feature Importance
imp = rfc.feature_importances_
names = data.iris.feature_names
zip(imp, names)
imp, names = zip(*sorted(zip(imp, names)))
plt.barh(range(len(names)), imp, align='center')
plt.yticks(range(len(names)), names)
plt.xlabel('Importance of Features')
plt.title('Importance of Each Feature')
plt.show()


