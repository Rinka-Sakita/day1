import numpy as np

docs = [["リンゴ", "リンゴ"], ["リンゴ", "レモン"], ["レモン", "ミカン"]] 
terms = ["リンゴ", "レモン", "ミカン"]

def tf(term: str, doc: list)->float:
    return doc.count(term) / len(doc)

def idf(term: str, docs: list)->float:
    n = len(docs)
    count = 0
    for i in docs:
        if term in i:
            count += 1
    return np.log10(n / count) + 1

def tf_idf(terms, docs):
    ans = np.zeros((len(docs), len(terms)))
    num_d = -1
    for doc in docs:
        num_d += 1
        num_t = -1
        for term in terms:
            num_t += 1
            ans[num_d][num_t] = tf(term, doc) * idf(term, docs)
    return ans 

if __name__ == "__main__":
    print(tf_idf(terms, docs))