dictionary = dict()
idx = [1, 5, 6, 7, 8, 9, 15, 16, 19]
s = "Hi He Lead Because Boron Could Not Oxidize Flourine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
transformed_s = s.replace(".", "")
words = transformed_s.split()
for i, word in enumerate(words, start = 1):
    if i in idx:
        dictionary[word[0]] = i
    else:
        dictionary[word[0:2]] = i
print(dictionary)