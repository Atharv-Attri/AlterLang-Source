import RAKE
import nltk
from nltk.tokenize import word_tokenize
import json
import re

try:
    with open("stoplist.json") as f:
        stoplist = json.load(f)
except:
    try:
        with open("./interpreter/stoplist.json") as f:
            stoplist = json.load(f)
    except:
        with open("./alterlang-source/interpreter/stoplist.json") as f:
            stoplist = json.load(f)


class Variable:
    def __init__(self, text):
        global stoplist
        self.text = text
        self.namelookup = ["NNP", "NNS", "NN", "JJS", "JJ", "DT"]
        self.stoplist = stoplist["variable"]
        self.tmp = ""

    def name(self):
        self.stop_dir = "./stoplist.txt"
        self.rake_object = RAKE.Rake(self.stop_dir)
        self.keywords = self.sort_tup(self.rake_object.run(self.text)[-10:])

    def sort_tup(self, tup):
        tup.sort(key=lambda x: x[1])
        return tup

    def get_name(self):
        self.tmp = word_tokenize(self.text)
        self.words = nltk.pos_tag(self.tmp)
        self.words = [i for i in self.words if i[0] not in self.stoplist]
        self.words = [i for i in self.words if i[1] in self.namelookup]
        return self.words[-1][0]

    def get_value(self):
        if self.text.count('"') == 2 or self.text.count("'") == 2:
            tmp = re.findall(r"\'(.+)\'", self.text)
            if len(tmp) == 0:
                tmp = re.findall(r"\"(.+)\"", self.text)
            return tmp[0]
        for i in ["True", "true", "False", "false"]:
            if i in self.text:
                return i
        self.tmp = word_tokenize(self.text)
        self.words = nltk.pos_tag(self.tmp)
        self.words = [i for i in self.words if i[0] not in self.stoplist]
        for i in self.words:
            if i[1] == "CD":
                return i[0]


class Whilel:
    def __init__(self, text):
        global stoplist
        self.text = text
        self.stoplist = stoplist["while"]
        self.tmp = ""

    def focus(self):
        for i in stoplist:
            self.text = self.text.replace(i, "")

    def boolreplace(self):
        self.text = re.sub(r"is [t/T]rue", "is True", self.text)
        self.text = re.sub(r"is [f/F]alse", "is False", self.text)

    def replace_discm(self):
        self.text = re.sub(r"{|:|->", "", self.text)
        self.text = re.sub(r"\(", "", self.text)
        self.text = re.sub(r"\)", "", self.text)

    def get_condition(self):
        self.focus()
        self.boolreplace()
        self.replace_discm()
        self.text = self.text.replace(" ", "")
        return self.text


class ifl:
    def __init__(self, text):
        global stoplist
        self.text = text
        self.stoplist = stoplist["if"]
        self.tmp = ""

    def focus(self):
        for i in stoplist:
            self.text = self.text.replace(i, "")
        self.text = self.text.replace("assuming", "")

    def boolreplace(self):
        self.text = re.sub(r"is ?[t/T]rue", " is True", self.text)
        self.text = re.sub(r"is ?[f/F]alse", " is False", self.text)

    def replace_discm(self):
        self.text = re.sub(r"{|:|->", "", self.text)
        self.text = re.sub(r"\(", "", self.text)
        self.text = re.sub(r"\)", "", self.text)

    def get_condition(self):
        self.focus()
        self.replace_discm()
        self.text = self.text.replace(" ", "")
        self.text = self.text.replace("and", " and ")
        self.boolreplace()
        self.text = self.text.replace("otherwise", "")
        self.text = self.text.replace("is", " is ")
        self.text = self.text.replace("False", " False ")
        return self.text
