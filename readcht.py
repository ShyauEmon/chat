data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)  # 從f拿出line放入lotty[]的list裡面

# 文字計數
wc = {}
for d in data:
    words = d.split()
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1

# 將出現超過100000次的字印出來
for word in wc:
    if wc[word] > 100000:
        print(word)

print("字典內共有", len(wc), "個Key")

# 讓使用者可自行查找文字出現次數
while True:
    x = input("請輸入要查找的字:")
    if x == "q":
        print("程式結束")
        break
    elif x in wc:
        print(x, "出現次數:", wc[x])
    else:
        print("查無此字")

