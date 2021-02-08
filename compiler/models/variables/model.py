from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
from textblob.blob import Blobber
from rich.console import Console
import pickle

console = Console()
print("")
with console.status("[bold green]Working on tasks...") as status:
    tasks = ["started", "loaded", "pickle made", "classified"]
    task = tasks.pop(0)
    console.log(f"{task} complete")
    train = [
        # tuples in the format of ("data","<pos/neg>")
    ]
    test = [
        # tuples in the format of ("data","<pos/neg>")
    ]
    with open("model.json", "r") as fp:
        cl = NaiveBayesClassifier(fp, format="json")
    task = tasks.pop(0)
    console.log(f"{task} complete")
    object = cl
    file = open("classifier.pickle", "wb")
    pickle.dump(object, file)
    task = tasks.pop(0)
    console.log(f"{task} complete")
    # Classify some text
    print(cl.classify("set the value of age to be 5"))  # "pos"
    print(cl.classify("while x is less than 33 ->"))  # "neg"
    task = tasks.pop(0)
    console.log(f"{task} complete")
