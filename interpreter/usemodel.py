import pickle
import time
from textblob import TextBlob


def load():
    try:
        cl = pickle.load(
            open(r"C:\Users\atharv\Documents\Alter\Alter-ML\classifier.pickle", "rb")
        )
    except:
        try:
            cl = pickle.load(
                open(
                    r"C:\Users\atharv\Documents\Alter\Alter-ML\classifier.pickle", "rb"
                )
            )
        except:
            cl = pickle.load(
                open(
                    r"C:\Users\atharv\Documents\Alter\Alter-ML\classifier.pickle",
                    "rb",
                )
            )
    return cl


def classify(text: str) -> bool:
    cl = load()
    blob = TextBlob(text, classifier=cl)
    out = blob.classify()
    if out == "neg":
        return False
    return True


if __name__ == "__main__":
    cl = load()
    t1 = time.time()
    blob = TextBlob("while x is 1 {", classifier=cl)
    print(blob.classify())
    print("Classifying took: ", time.time() - t1)
    t1 = time.time()
    blob = TextBlob("set x to 55", classifier=cl)
    print(blob.classify())
    print("Classifying took: ", time.time() - t1)
    t1 = time.time()
    blob = TextBlob("name equals 'hello'", classifier=cl)
    print(blob.classify())
    print("Classifying took: ", time.time() - t1)
    t1 = time.time()
    blob = TextBlob("\n", classifier=cl)
    print(blob.classify())
    print("Classifying took: ", time.time() - t1)
