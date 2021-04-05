if __name__ == "__main__":
    data={}
    with open("SimplifiedChinese.tsv", encoding="utf-8") as f:
        lines=f.readlines()
        for line in lines:
            seg = line.split("\t")
            data[seg[2]]=seg[3][:-1]
    with open("new.tsv", encoding="utf-8") as f:
        with open("new2.tsv", "w", encoding="utf-8") as wf:
            lines=f.readlines()
            for line in lines:
                seg = line.split("\t")
                wf.write(f"{line}{data[seg[2]] if len(seg[2])>0 else ''}\n")
