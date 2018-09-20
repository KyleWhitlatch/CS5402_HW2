from id3 import Id3Estimator, export_text
import numpy as np


def main():
    feature_names = ["Opponent", "Home/Away", "AP Top 25", "Media"]

    X = np.array([['Texas', 'Home', 'Out', '1-NBC'],
                  ['Virginia', 'Away', 'Out', '4-ABC'],
                  ['GeorgiaTech', 'Home', 'In', '1-NBC'],
                  ['UMass', 'Home', 'Out', '1-NBC'],
                  ['Clemson', 'Away', 'In', '4-ABC'],
                  ['Navy', 'Home', 'Out', '1-NBC'],
                  ['USC', 'Home', 'In', '1-NBC'],
                  ['Temple', 'Away', 'Out', '4-ABC'],
                  ['PITT', 'Away', 'Out', '4-ABC'],
                  ['WakeForest', 'Home', 'Out', '1-NBC'],
                  ['BostonCollege', 'Away', 'Out', '1-NBC'],
                  ['Stanford', 'Away', 'In', '3-FOX'],
                  ['Texas', 'Away', 'Out', '4-ABC'],
                  ['Nevada', 'Home', 'Out', '1-NBC'],
                  ['MichiganState', 'Home', 'Out', '1-NBC'],
                  ['Duke', 'Home', 'Out', '1-NBC'],
                  ['Syracuse', 'Home', 'Out', '2-ESPN'],
                  ['NorthCarolinaState', 'Away', 'Out', '4-ABC'],
                  ['Stanford', 'Home', 'In', '1-NBC'],
                  ['MiamiFlorida', 'Home', 'Out', '1-NBC'],
                  ['Navy', 'Home', 'Out', '5-CBS'],
                  ['Army', 'Home', 'Out', '1-NBC'],
                  ['VirginiaTech', 'Home', 'In', '1-NBC'],
                  ['USC', 'Away', 'In', '4-ABC']])

    y = np.array(["Win",
                  "Win",
                  "Win",
                  "Win",
                  "Lose",
                  "Win",
                  "Win",
                  "Win",
                  "Win",
                  "Win",
                  "Win",
                  "Lose",
                  "Lose",
                  "Win",
                  "Lose",
                  "Lose",
                  "Win",
                  "Lose",
                  "Lose",
                  "Win",
                  "Lose",
                  "Win",
                  "Lose",
                  "Lose"])

    clf = Id3Estimator()
    clf.fit(X, y, check_input=True)
    print("Training:")
    print(export_text(clf.tree_, feature_names))
    testing = [["Temple", "Home", "Out", "1-NBC"],
               # ["Georgia", "Home", "In", "1-NBC"],
               ["BostonCollege", "Away", "Out", "2-ESPN"],
               ["MichiganState", "Away", "Out", "3-FOX"],
               # ["MiamiOhio", "Home", "Out", "1-NBC"],
               # ["NorthCarolina", "Away", "Out", "4-ABC"],
               ["USC", "Home", "In", "1-NBC"],
               ["NorthCarolinaState", "Home", "Out", "1-NBC"],
               ["WakeForest", "Home", "Out", "1-NBC"],
               ["MiamiFlorida", "Away", "In", "4-ABC"],
               ["Navy", "Home", "Out", "1-NBC"],
               ["Stanford", "Away", "In", "4-ABC"]]
    print("\n\nTesting:")
    print(clf.predict(testing))

if __name__ == "__main__":
    main()
