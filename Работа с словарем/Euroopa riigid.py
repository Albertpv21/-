from module1 import*
from gtts import gTTS
import os 

countries_dict={"Albaania":"Tirana","Andorra":"Andorra la Vella","Armeenia":"Jerevan","Aserbaidžaan":"Bakuu","Austria":"Viin","Belgia":"Brüssel","Bulgaaria":"Sofia","Eesti":"Tallinn","Gruusia":"Thbilisi"}
print(countries_dict )
o=gTTS(text=countries_dict["Albaania"],lang="et",slow=True).save("heli.mp3")
os.system("heli.mp3")
while True:
    print("Tere,vaatame millised on riigid ja nende pealinnad")
    print("1 - Uurige välja riigi pealinn või vastupidi,2 -uus pealinn ja riik,3- kustutamine")
    s=input()
    if s=="1":
        v=input("Kas otsime riiki pealinna (1) või pealinna järgi (2)? ")
        countries(countries_dict,v)
    elif s=="2":
        otsing(countries_dict)
    elif s=="3":
        kustutamine(countries_dict)
