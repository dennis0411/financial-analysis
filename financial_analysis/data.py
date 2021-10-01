from sklearn import datasets
from sklearn.model_selection import train_test_split
import pandas as pd
from pandas_ods_reader import read_ods

iris = datasets.load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)  # 實作上加入 random_state=42 固定結果


# print(iris.keys()) # 資料為 dictionary array,可用pandas針對字典Keys內容預處理


def read_data(symbol='spx', style='csv'):
    if style == 'ods':
        df = read_ods(f'{symbol}.ods')
    else:
        df = pd.read_csv(f'{symbol}.csv')
    return df
