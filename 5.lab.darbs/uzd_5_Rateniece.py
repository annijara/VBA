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
unikali_datumi = lapas[0][["Datums", "Skaits"]].groupby("Datums").count()
unikali_datumi.insert(0, "Datums", unikali_datumi.index)
lapas.append(unikali_datumi)

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