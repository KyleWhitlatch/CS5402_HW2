import pyC45


def main():
    X = [["Opponent", "Home/Away", "AP Top 25", "Media"],
         ['Texas', 'Home', 'Out', '1-NBC'],
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
         ['USC', 'Away', 'In', '4-ABC']
         ]
    Y = ["Win",
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
                  "Lose"]
    pyC45.train(X, Y, "T5c45.xml")

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

    #pyC45.predict("T5c45.xml", testing)

if __name__ == "__main__":
    main()