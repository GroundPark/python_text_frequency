print("----------------------------------------------")
txt = input('     ')
txt2 = list(txt)
print("----------------------------------------------")
print("문자개수 :", len(txt))

def freq(txt2):
    Dic={}
    for i in txt2:
        Cnt=txt2.count(i);
        Dic[i]=Cnt
    for cnts in Dic:
        print(cnts,":",Dic[cnts])
    return

print("----------------------------------------------")
freq(txt2)
print("----------------------------------------------")
