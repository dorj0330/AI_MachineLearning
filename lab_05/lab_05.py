import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report
from sklearn.model_selection import train_test_split


def _importData():
    global x, y
    ds = pd.read_csv('diabetes_pp.csv')
    y = ds['Outcome']
    x = ds.drop('Outcome', axis=1)


_importData()


def _split(size):
    global x_train, x_test, y_train, y_test
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=size)


_split(0.2)


def _createModel():
    global dt_model
    dt_model = DecisionTreeClassifier(criterion='entropy')


_createModel()


def _fit():
    dt_model.fit(x_train, y_train)


_fit()


def _predict():
    global y_pred
    y_pred = dt_model.predict(x_test)


_predict()


def _report():
    report = classification_report(y_test, y_pred)
    print(report)


_report()


def _conf_matrix():
    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(cm)
    disp.plot()
    print(cm)


_conf_matrix()


def _drawTree():
    class_names = y.astype(str).unique().tolist()

    dot_file = export_graphviz(dt_model, out_file='diabetes.dot',
                               feature_names=x.columns,
                               class_names=class_names,
                               filled=True)


_drawTree()
