def info():
    järjend=[]
    sõnastik={}
    with open ("küsimused_ja_vastused.txt",encoding="UTF-8") as f:
        for rida in f:
            rida=rida.strip().split(";")
            järjend.append(rida[0])
            sõnastik[rida[0]]=rida[1]
        return järjend, sõnastik
