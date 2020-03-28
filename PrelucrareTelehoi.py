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


print("Inainte de modificare: ", masini_toyota)
reducere(masini_toyota)
print("Dupa modificare: ", masini_toyota)





