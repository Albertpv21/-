from random import *
for line in file:
    k,v=line.strip().split("-")
    TextFile1[k.strip()]=v.strip()
def countries(d:dict, v:int):
    keys_list=(list(d.keys()))
    values_list=(list(d.values()))
    if v=="1":
        s=[]
        a=(input("Kirjuta Pealinn: ")).capitalize()
        a.title()
        for i in values_list:
            if i==a:
                for i in range(len(values_list)):
                    if values_list[i]==a:
                        s.append(int(i))
                        print("Riik -", keys_list[i],":", "Pealinn -", values_list[i])
    else:
        c=(input("Kirjuta riik: ")).capitalize()
        a=d.get(c)
        print("Riik -", c ,":", "Pealinn -", a)
    return
def otsing(countries_dict):
    c=input("Kirjuta Pealinn=")
    b=input("Kirjuta Riik=")
    countries_dict.update({c: b})
    print("Riik -", b ,":", "Pealinn -", c)
def kustutamine(countries_dict):
    b=input("Kirjutage Riiki mille tahate kustutada->")
    countries_dict.pop(b)
    print("Kustutatud Riik-",b,)
def uuring(countries_dict):
    v=int(input("Tere kas sa tahad kontrollima oma teadmisi? 1-Ja, 2-Ei"))
    if v==1:
        n=randint(0,9)
        print(countries_dict[c[n])
        print(countries_dict[c[randint(0,9)]])



        

    



