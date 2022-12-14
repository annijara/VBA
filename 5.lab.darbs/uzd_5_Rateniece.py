import pandas
fails = pandas.ExcelFile("dati_masiviem.xlsx")
lapas = []
for lapa in fails.sheet_names:
    lapas.append(fails.parse(lapa))
 
lapas[0]["Cena"] = lapas[0]["Pašizmaksa"] * 1.31
cena = lapas[0]["Cena"]

lapas[0]["Kopā"] = lapas[0]["Skaits"] * lapas[0]["Cena"]
kopā = lapas[0]["Kopā"]

lapas[0]["Peļņa"] = kopā - (lapas[0]["Pašizmaksa"]*lapas[0]["Skaits"]* 1.21)
peļņa = lapas[0]["Peļņa"]

#d = (kopā, peļņa)

""" parvietota_rinda = pandas.DataFrame(data = kopā).T
parvietota_rinda = parvietota_rinda.reindex(columns=lapas[0].columns)
print(parvietota_rinda) """



lapas_nr = 1
with pandas.ExcelWriter("rezult.xlsx") as fails:
    for lapa in lapas:
        lapa.to_excel(fails, sheet_name= str(lapas_nr), index=False)
        lapas_nr += 1