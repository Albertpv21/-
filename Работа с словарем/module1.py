def countries(d:dict, v:int):
    keys_list=(list(d.keys()))
    values_list=(list(d.values()))
    if v=="1":
        p=[]
        capital=(input("Pealinn: ")).capitalize()
        capital.title()
        for i in values_list:
            if i==capital:
                for i in range(len(values_list)):
                    if values_list[i]==capital:
                        p.append(int(i))
                        print("Riik -", keys_list[i],":", "Pealinn -", values_list[i])
    else:
        country=(input("Vali riiki: ")).capitalize()
        a=d.get(country)
        print("Riik -", country ,":", "Pealinn -", a)
    return

