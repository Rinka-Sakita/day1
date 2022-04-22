docs = [["リンゴ", "リンゴ"], ["リンゴ", "レモン"], ["レモン", "ミカン"]]
terms = ["リンゴ", "レモン", "ミカン"]

def tf(term: str, doc: list)->float:
    return doc.count(term) / len(doc)

for i in docs:
    for j in terms:
        print("tf(", j, ",", i, ") =", tf(j, i), end = "  ")
    print("")