from id3 import Id3Estimator, export_text
import numpy as np


def main():
    feature_names = ["outlook",
                 "temperature",
                 "humidity",
                 "windy"]

    X = np.array([['sunny', 'hot', 'high', 'false'],
                  ['sunny', 'hot', 'high', 'true'],
                  ['overcast', 'hot', 'high', 'false'],
                  ['rainy', 'mild', 'high', 'false'],
                  ['rainy', 'cool', 'normal', 'false'],
                  ['rainy', 'cool', 'normal', 'true'],
                  ['overcast', 'cool', 'normal', 'true'],
                  ['sunny', 'mild', 'high', 'false'],
                  ['sunny', 'cool', 'normal', 'false'],
                  ['rainy', 'mild', 'normal', 'false'],
                  ['sunny', 'hot', 'high', 'false'],
                  ['sunny', 'hot', 'high', 'false'],
                  ['sunny', 'hot', 'high', 'false'],
                  ['sunny', 'hot', 'high', 'false'],])

    y = np.array(["win",
                  "lose",
                  "win",
                  "win",
                  "win",
                  "win"])

    clf = Id3Estimator()
    clf.fit(X, y, check_input=True)

    print(export_text(clf.tree_, feature_names))


if __name__ == "__main__":
    main()