import numpy as np

docs = [["リンゴ", "リンゴ"], ["リンゴ", "レモン"], ["レモン", "ミカン"]] 
terms = ["リンゴ", "レモン", "ミカン"]

def idf(term: str, docs: list)->float:
    n = len(docs)
    count = 0
    for i in docs:
        if term in i:
            count += 1
    return np.log10(n / count) + 1

for j in terms:
    print("idf(", j, ") = ", idf(j, docs))