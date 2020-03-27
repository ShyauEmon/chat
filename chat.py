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
    new = []
    person = None
    for line in lines:
        if line == "阿倫":
            person = "阿倫"
            continue
        elif line == "湯姆":
            person = "湯姆"
            continue
        elif person:
            new.append(person + ": " + line)
    return new


# 存入檔案
def write_file(filename, lines):
    with open(filename, "w", encoding='utf-8') as f:
        for line in lines:
            f.write(line + "\n")


# 讀檔 轉檔 存入
def main():
    lines = read_file("input.txt")
    lines = convert(lines)
    write_file("output.txt", lines)


main()
