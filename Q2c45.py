import pyC45


def main():
    X = [["outlook", "temperature", "humidity", "windy"],
            ['sunny', 'hot', 'high', 'false'],
            ['sunny', 'hot', 'high', 'true'],
            ['overcast', 'hot', 'high', 'false'],
            ['rainy', 'mild', 'high', 'false'],
            ['rainy', 'cool', 'normal', 'false'],
            ['rainy', 'cool', 'normal', 'true'],
            ['overcast', 'cool', 'normal', 'true'],
            ['sunny', 'mild', 'high', 'false'],
            ['sunny', 'cool', 'normal', 'false'],
            ['rainy', 'mild', 'normal', 'false'],
            ['sunny', 'mild', 'normal', 'true'],
            ['overcast', 'mild', 'high', 'true'],
            ['overcast', 'hot', 'normal', 'false'],
            ['rainy', 'mild', 'high', 'true']
         ]
    Y = ["No",
                  "No",
                  "Yes",
                  "Yes",
                  "Yes",
                  "No",
                  "Yes",
                  "No",
                  "Yes",
                  "Yes",
                  "Yes",
                  "Yes",
                  "Yes",
                  "No"]
    pyC45.train(X,Y,"Q2c45.xml")


if __name__ == "__main__":
    main()