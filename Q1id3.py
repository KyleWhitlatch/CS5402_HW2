from id3 import Id3Estimator, export_text
import numpy as np


def main():
    feature_names = ["home/away",
                 "top25",
                 "media"]

    X = np.array([['home', 'out', '1-nbc'],
                  ['home', 'in', '1-nbc'],
                  ['away', 'out', '2-espn'],
                  ['away', 'out', '3-fox'],
                  ['home', 'out', '1-nbc'],
                  ['away', 'out', '4-abc']])

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