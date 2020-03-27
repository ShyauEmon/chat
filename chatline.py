import os


# 讀取檔案
def read_file(filename):
    lines = []
    with open(filename, "r", encoding="utf-8") as f:  # 如果讀檔後輸出前面有編碼資料可改encoding="utf-8-sig"
        for line in f:
            lines.append(line.strip())
    # 印出檔案內資料
    print(lines)
    return lines


# 轉換檔案
def convert(lines):
    s_word_count = 0
    s_sticker_count = 0
    l_word_count = 0
    l_sticker_count = 0
    for line in lines:
        s = line.split(" ")
        time = s[0]
        name = s[1]
        if name == "世昕":
            if s[2] == "貼圖":
                s_sticker_count += 1
            else:
                for m in s[2:]:
                    s_word_count += len(m)
        elif name == "Lai":
            if s[2] == "貼圖":
                l_sticker_count += 1
            else:
                for m in s[2:]:
                    l_word_count += len(m)
    print("世昕說了", s_word_count, "字,使用貼圖:", s_sticker_count, "次")
    print("Lai說了", l_word_count, "字,使用貼圖:", l_sticker_count, "次")


# 存入檔案
def write_file(filename, lines):
    with open(filename, "w", encoding='utf-8') as f:
        for line in lines:
            f.write(line + "\n")


# 讀檔 轉檔 存入
def main():
    lines = read_file("lineinput.txt")
    lines = convert(lines)
    #write_file("lineput.txt", lines)


main()
