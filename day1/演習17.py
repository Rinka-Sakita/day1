import numpy as np
from nlp import 演習15
from nlp import 演習16

docs = [['リンゴ', 'リンゴ', 'リンゴ'], ['リンゴ', 'レモン', 'レモン', 'ミカン'], ['リンゴ', 'イチゴ', 'ミカン'], ['レモン', 'イチゴ', 'ミカン'], ['ミカン', 'ミカン', 'ブドウ', 'ブドウ']]
terms = ['リンゴ', 'ブドウ', 'ミカン', 'レモン', 'イチゴ']
tf_idf = 演習15.tf_idf(terms, docs)
l = len(tf_idf)
ans = np.zeros((l, l))

for i in range(l):
    for j in range(l):
        ans[i][j] = 演習16.cosine_sim(tf_idf[i], tf_idf[j])

print(ans)