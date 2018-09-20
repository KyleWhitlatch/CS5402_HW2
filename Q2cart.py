from sklearn.tree import DecisionTreeClassifier, export_graphviz
import graphviz
import numpy as np
import os

def main():
    tree = DecisionTreeClassifier()
    x = np.array([
        ['1', '1', '1', '0'],
        ['1', '1', '1', '1'],
        ['2', '1', '1', '0'],
        ['3', '2', '1', '1'],
        ['3', '3', '2', '0'],
        ['3', '3', '2', '1'],
        ['2', '3', '2', '1'],
        ['1', '2', '1', '0'],
        ['1', '3', '2', '0'],
        ['3', '2', '2', '0'],
        ['1', '2', '2', '1'],
        ['2', '2', '1', '1'],
        ['2', '1', '2', '0'],
        ['3', '2', '1', '1']])

    y = np.array(["0",
                  "0",
                  "1",
                  "1",
                  "1",
                  "0",
                  "1",
                  "0",
                  "1",
                  "1",
                  "1",
                  "1",
                  "1",
                  "0"])
    clf = tree.fit(X=x,y=y)
    data = export_graphviz(clf,
                            out_file="q2.dot",
                            feature_names=["outlook", "temperature", "humidity", "windy"],
                            class_names=['not played', 'played']
                            )

    predict = tree.predict([['3', '1', '1', '0']])
    print("Running test case: 0 is false, 1 is true")
    print(predict)

#IMPORTANT:
#THIS WILL CREATE A FILE q2.dot USING www.webgraphviz.com TO VISUALIZE

if __name__ == "__main__":
    main()