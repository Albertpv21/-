from random import *
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
        c=(input("Kirjuta Riik: ")).capitalize()
        a=d.get(c)
        print("Riik -", c ,":", "Pealinn -", a)
    return
def otsing(countries_dict):
    c=input("Kirjuta Riik=")
    b=input("Kirjuta Pealinn=")
    countries_dict.update({c: b})
    print("Pealinn -", b ,":", "Riik -", c)
def kustutamine(countries_dict):
    b=input("Kirjutage Riiki mille tahate kustutada->")
    countries_dict.pop(b)
    print("Kustutatud Riik-",b,)
def teadmet(countrie_dict):
    a=["Albaania","Andorra","Armeenia","Aserbaidžaan","Austria","Belgia","Bulgaaria","Eesti","Gruusia"]
    b=["Tirana","Andorra la Vella","Jerevan","Bakuu","Viin","Brüssel","Sofia","Tallinn","Thbilisi"]




        

    



