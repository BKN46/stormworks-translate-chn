def strproc(a):
    return a.replace('\t','').replace('\n','')

if __name__ == "__main__":
    data={}
    TAB='\t'
    with open("SimplifiedChinese.tsv", encoding="utf-8") as f:
        lines=f.readlines()
        for line in lines:
            seg = line.split("\t")
            data[seg[2]]=seg[3][:-1]
    with open("raw.tsv", encoding="utf-8") as f:
        with open("test.tsv", "w", encoding="utf-8") as wf:
            lines=f.readlines()
            for line in lines:
                seg = line.split("\t")
                line = '\t'.join(seg[:-1]).replace('\n','')
                wf.write(f"{line}{TAB}{strproc(data[seg[2]]) if len(seg[2])>0 else ''}\n")
