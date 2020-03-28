import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#import fisiere csv
date = pd.read_csv('python.csv')
comenzi = pd.read_csv('comenzi.csv')

# #prelucrari statistice simple
# print("Numar modele:", end=' ')
# print(date['Model'].count(), end='\n\n')
#
# luni = date.columns[2:]
#
# print("Vanzari lunare totale:")
# print(round(date[luni].sum()), end='\n\n')
#
# print("Cea mai mare vanzare intr-o luna:", end=' ')
# print(date[luni].sum().max(), end='\n\n')
#
# print("Vanzari medii pe luna:")
# print(round(date[luni].mean()), end='\n\n')
#
# vanzare_medie = date[luni].mean().mean()
# print("Vanzarea medie dintr-o luna pentru un model:", end=' ')
# print(round(vanzare_medie), end='\n\n')
#
# #grupare si agregare
# print("Comenzi pentru fiecare model:")
# print(comenzi.groupby(['Model']).agg({'Cantitate':sum}))
#
# #tratare valori lipsa din C-HR
# date.fillna(vanzare_medie, inplace=True)
# print(date)
#
# #reprezentare grafica - distributia vanzarilor din anul 2018, Europa
# labels = date['Model'].tolist()
# sizes = date.sum(axis=1).tolist()
# plt.pie(sizes, labels=labels)
# plt.show()

# #Modificarea datelor in pachetul pandas
# date_2 = date
# date_2['Total'] = round(date_2.sum(axis=1))
# preturi_noi = [25000, 22000, 23500, 20000, 15000, 12000]
# date_2['Pret'] = preturi_noi
# date_2['Venit'] = round(date_2.Pret * date_2.Total/1000000)
# print(date_2)





