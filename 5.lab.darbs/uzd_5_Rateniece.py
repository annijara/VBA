import pandas
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

grupetie_dati = lapas[0]["Datums"]
lapas.append(grupetie_dati)
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
if lapas[0]["Datums"] == "07.10.2020":
    lapas.append(lapas[0])


 
lapas_nr = 1
with pandas.ExcelWriter("rezult.xlsx") as fails:
    for lapa in lapas:
        lapa.to_excel(fails, sheet_name= str(lapas_nr), index=False)
        lapas_nr += 1