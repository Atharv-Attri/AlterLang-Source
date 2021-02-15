import pickle
import time
from textblob import TextBlob


def load():
    try:
        cl = pickle.load(open("./models/variables/classifier.pickle", "rb"))
    except:
        cl = pickle.load(open("./compiler/models/variables/classifier.pickle", "rb"))

    return cl


def run(text: str) -> bool:
    cl = load()
    blob = TextBlob(text, classifier=cl)
    out = blob.classify()
    if out == "neg":
        return False
    return True


if __name__ == "__main__":
    t1 = time.time()
    blob = TextBlob("while x is 1:", classifier=cl)
    print(blob.classify())
    print("Classifying took: ", time.time() - t1)
    t1 = time.time()
    blob = TextBlob("x=4", classifier=cl)
    print(blob.classify())
    print("Classifying took: ", time.time() - t1)
    t1 = time.time()
    blob = TextBlob("name = 'hello'", classifier=cl)
    print(blob.classify())
    print("Classifying took: ", time.time() - t1)