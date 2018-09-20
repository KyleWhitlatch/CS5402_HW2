from sklearn.tree import DecisionTreeClassifier, export_graphviz
import graphviz
import numpy as np

def main():
    x = np.array([
            ['0', '0', '1'],
            ['0', '1', '1'],
            ['0', '0', '2'],
            ['0', '0', '3'],
            ['0', '0', '1'],
            ['0', '0', '4']])

    y = np.array([1,
         0,
         1,
         1,
         1,
         1])
    clf = DecisionTreeClassifier().fit(X=x,y=y)
    data = export_graphviz(clf,
                            out_file="q1.dot",
                            feature_names=["home/away", "top25", "media"],
                            class_names=['in top25', 'out of top25']
                            )
    data = graphviz.Source(data)
    data

#IMPORTANT:
##THIS WILL CREATE A FILE q1.dot USING www.webgraphviz.com TO VISUALIZE

if __name__ == "__main__":
    main()