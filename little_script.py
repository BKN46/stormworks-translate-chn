if __name__ == "__main__":
    count = 0
    with open("res.tsv", encoding="utf-8") as f:
    # with open("SimplifiedChinese.tsv", encoding="utf-8") as f:
        with open("quest.tsv", "w", encoding="utf-8") as fr:
            lines = f.readlines()
            for line in lines:
                seg = line.split("\t")
                if len(seg) < 4 or (len(seg[2]) > 1 and len(seg[3]) < 2):
                    count += 1
                    print(line.replace("\n", ""), file=fr)
