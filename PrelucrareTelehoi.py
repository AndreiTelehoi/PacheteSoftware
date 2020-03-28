import pandas as pd

# 1. Functii cu structuri conditionale si repetitive

# Sa se defineasca o functie care pentru fiecare model de masina cu pretul mai mare de 15.000 euro, sa se aplice o reducere de 5%.
# Sa se apeleze functia pentru dictionarul dat.

masini_toyota = {
    "masina1" : {
        "model" : "corolla",
        "pret" : 26000
    },
    "masina2" : {
        "model" : "prius",
        "pret" : 22500
    },
    "masina3" : {
        "model" : "rav4",
        "pret" : 24000
    },
    "masina4" : {
        "model" : "c-hr",
        "pret" : 20000
    },
    "masina5" : {
        "model" : "yaris",
        "pret" : 14500
    },
    "masina6" : {
        "model" : "aygo",
        "pret" : 11500
    }
}


def reducere (masini) :
    for masina in masini.items():
        if masina[1]["pret"] > 15000:
            masina[1]["pret"] = masina[1]["pret"] * (1 - 0.05)


print("Inainte de modificare: ", masini_toyota, "\n")
reducere(masini_toyota)
print("Dupa modificare: ", masini_toyota, "\n")


# 3. Accesarea datelor cu loc si iloc

df_masini = pd.read_csv('python.csv')

# a) Sa se afiseze din fisierul csv primele trei modele de masini si pretul aferent, folosind iloc

print(df_masini.iloc[0:3, 0:2], "\n")

# b) Sa se afiseze pt urmatoarele 3 masini modelul, pretul aferent si vanzarile pentru lunile ianuarie si februarie, folosind loc

print(df_masini.loc[3:5, "Model":"Februarie"], "\n")

# 5. Functii de grup

# Sa se afiseze pretul minim, pretul maxim si pretul mediu

pret_minim = df_masini["Pret"].min()
print("Pretul minim este: ", pret_minim)

pret_maxim = df_masini["Pret"].max()
print("Pretul maxim este: ", pret_maxim)

pret_mediu = df_masini["Pret"].mean()
print("Pretul maxim este: ", pret_mediu)

