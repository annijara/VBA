import pandas
import pandas as pd
fails = pandas.ExcelFile("dati_masiviem.xlsx")
lapas = []
for lapa in fails.sheet_names:
    lapas.append(fails.parse(lapa))
    
# 1.uzdevums 
lapas[0]["Cena"] = lapas[0]["Pašizmaksa"] * 1.31
cena = lapas[0]["Cena"]
lapas[0]["Kopā"] = lapas[0]["Skaits"] * lapas[0]["Cena"]
kopā = lapas[0]["Kopā"]
lapas[0]["Peļņa"] = kopā - (lapas[0]["Pašizmaksa"]*lapas[0]["Skaits"]* 1.21)
peļņa = lapas[0]["Peļņa"]

#2.uzdevums
ieliekama_rinda = lapas[0][["Skaits","Cena", "Pašizmaksa", "Peļņa", "Kopā"]].sum()
parvietota_rinda = pandas.DataFrame(data = ieliekama_rinda).T
parvietota_rinda = parvietota_rinda.reindex(columns=lapas[0].columns)
lapas.append(lapas[0])
lapas[1] = lapas[1].append(parvietota_rinda) 

#3.uzdevums
lapas.append(lapas[0]["Datums"])
k = lapas[2]
d = k.unique()
lapas[2] = k.append(d)
print (d)
#df2 = pd.unique(lapas[0][['Datums']].values.ravel())
""" df = lapas[0]["Datums"]

lapas.append(k) """
#df['species'].nunique()
""" grupetie_dati = lapas[0]["Datums"]
df = _FileRead.readFile("dati_masiviem.xlsx")

unique = df.drop_duplicates('Datums')
lapas.append(unique) """
""" #lapas.append()

datumi = dati['Datums'].value_counts()
#print(dati['Datums'].value_counts())
lapas[2] = lapas[2].append(datumi) """
""" dati = pandas.read_excel(fails)

df = dati.groupby("Datums").nunique()
#
#lapas[2]["Skaits"] = df
lapas.append(df)
#print (grupetie_dati)
 """
 
#4.uzdevums

lapas.append(lapas[0])
atrasts = lapas[3]['Datums'] == '2020-10-07'
lapas[3] = lapas[3][atrasts]
ieliekama_rinda = lapas[3][["Skaits"]].sum()
parvietota_rinda = pandas.DataFrame(data = ieliekama_rinda).T
parvietota_rinda = parvietota_rinda.reindex(columns=lapas[3].columns)
lapas[3] = lapas[3].append(parvietota_rinda) 



lapas_nr = 1
with pandas.ExcelWriter("rezult.xlsx") as fails:
    for lapa in lapas:
        lapa.to_excel(fails, sheet_name= str(lapas_nr), index=False)
        lapas_nr += 1