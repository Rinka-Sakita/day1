s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
transformed_s = s.replace(",", "").replace(".", "")  # 不要なカンマ、ピリオドを除去
words = transformed_s.split()  # 単語に分解
list = [len(word) for word in words]  # 文字数を並べたリスト
print(list)  # 表示