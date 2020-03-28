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
print("Pretul maxim este: ", pret_mediu, "\n")

# 7. Stergere de coloane si inregistrari

# a) sa se stearga inregistrarea pentru modelul CH-R

df_masini_fara_CHR = df_masini.set_index("Model")
df_masini_fara_CHR = df_masini_fara_CHR.drop("C-HR", axis=0)
print("Tabelul fara CH-R: \n", df_masini_fara_CHR, "\n")

# b) sa se stearga coloana cu vanzarile de pe luna noiembrie

df_masini_fara_noiembrie = df_masini.drop(columns="Noiembrie")
print("Tabelul fara noiembrie: \n", df_masini_fara_noiembrie, "\n")

# 9. Prelucrarea seturilor de date cu merge/join
# Sa se realizeze un inner merge pentru tabelele comenzi si importatori, dupa numarul comenzii, astfel incat sa fie vizibile
# numarul comenzii, modelul, cantitatea si numele importatorului

df_comenzi = pd.read_csv("comenzi.csv")
df_importatori = pd.read_csv("importatori.csv")
df_combinat = pd.merge(df_comenzi, df_importatori[["Numar Comanda", "Nume"]], on="Numar Comanda")
print(df_combinat)



