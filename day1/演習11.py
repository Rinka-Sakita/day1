with open('./dataset/data.txt', 'r') as f:
    file_data = f.readlines()
    for line in file_data:
        clean_line = line.strip()
        print(clean_line)