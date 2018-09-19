import pyC45


def main():
    X = [["home/away",
                 "top25",
                 "media"],
         ['home', 'out', '1-nbc'],
         ['home', 'in', '1-nbc'],
         ['away', 'out', '2-espn'],
         ['away', 'out', '3-fox'],
         ['home', 'out', '1-nbc'],
         ['away', 'out', '4-abc']
         ]
    Y = ["win",
                  "lose",
                  "win",
                  "win",
                  "win",
                  "win"]
    pyC45.train(X,Y,"Q1c45.xml")


if __name__ == "__main__":
    main()