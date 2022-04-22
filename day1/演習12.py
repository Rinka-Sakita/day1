docs = []
terms = []

with open('./dataset/data.txt', 'r') as f:
    file_data = f.readlines()
    for line in file_data:
        clean_line = line.strip()
        all = clean_line.split("と")
        docs.append(all)
        # 重複しないようにリストに追加
        for i in all:  
            if i not in terms:
                terms.append(i)

print("docs:", docs)
print("terms:", terms)