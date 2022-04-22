import sys
text = sys.argv[1:]

def n_gram(target: list, n: int)->list:
    """基準を1文字ずつずらしながらn文字分抜き出す"""
    return [target[idx:idx + n] for idx in range(len(target) - n + 1)]

print("単語bi-gram:", n_gram(text, 2))
print("文字bi-gram:", n_gram("".join(text), 2))
