from module1 import*

countries_dict={"Albaania":"Tirana","Andorra":"Andorra la Vella","Armeenia":"Jerevan","Aserbaidžaan":"Bakuu","Austria":"Viin","Belgia":"Brüssel","Bulgaaria":"Sofia","Eesti":"Tallinn","Gruusia":"Thbilisi"}
print(countries_dict )
while True:
    print("Tere,vaatame millised on riigid ja nende pealinnad")
    print("1 - Uurige välja riigi pealinn või vastupidi")
    s=input()
    if s=="1":
        v=input("Kas otsime riiki pealinna -1 või pealinna 2- järgi?")
        countries(countries_dict,v)