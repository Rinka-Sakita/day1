import sys
import random

def typoglycemia(text: str)->str:
    """入力文章でタイポグリセミア"""

    def random_word(word: str)->str:
        """文章を構成している単語の文字を並べ替える"""
        if len(word) < 4:  # 3文字以下はそのまま
            return word
        arr = list(word[1:-1])  
        random.shuffle(arr)  # 先頭と末尾以外をランダムに並び替え
        return word[0] + "".join(arr) + word[-1]  # 先頭と末尾を加えて返す
    
    return " ".join(list(map(random_word, text.split())))  # 単語の数だけ繰り返し、リストにしてから文字列にする

text = " ".join(sys.argv[1:])  # コマンドラインで受け取ったリストを文字列にする

print(typoglycemia(text))