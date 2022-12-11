import pandas
fails = pandas.ExcelFile("dati_masiviem.xlsx")
lapas = []
for lapa in fails.sheet_names:
    lapas.append(fails.parse(lapa))
print(lapas[0].shape)
print(lapas[0]["Nosaukums"]) 
lapas[0]["Cena"] = lapas[0]["Pašizmaksa"]* 1.21
#print(lapas[0]["Cena"])

ieliekama_rinda = lapas[0][["Skaits","Cena"]].sum()
#print("ieliekama rinda", ieliekama_rinda)
parvietota_rinda = pandas.DataFrame(data = ieliekama_rinda).T
print("----------")
#print(parvietota_rinda)
parvietota_rinda = parvietota_rinda.reindex(columns=lapas[0].columns)
#print(parvietota_rinda)

lapas.append(lapas[0])
lapas[1] = lapas[1].append(parvietota_rinda)
#print(lapas[1])

grupetie_dati = lapas[0][["Datums", "Skaits"]].groupby('Datums').sum()
#print(grupetie_dati)

grupetie_dati.insert(0,'Datums2', grupetie_dati.index)
#print(grupetie_dati)
lapas.append(grupetie_dati)

atrasts = lapas[2]["Datums2"] == "2020-09-09"
print(lapas[2][atrasts])

lapas_nr = 1
with pandas.ExcelWriter("jauns_fails2.xlsx") as fails:
    for lapa in lapas:
        lapa.to_excel(fails, sheet_name=str(lapas_nr), index=False)
        lapas_nr +=1





