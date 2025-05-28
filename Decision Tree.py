from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, export_text

def decision_tree_example():
    iris = load_iris()
    X, y = iris.data, iris.target
    clf = DecisionTreeClassifier()
    clf.fit(X, y)
    tree_rules = export_text(clf, feature_names=iris['feature_names'])
    print(tree_rules)

decision_tree_example()
