import pandas
fails = pandas.ExcelFile("dati_masiviem.xlsx")
lapas = []
for lapa in fails.sheet_names:
    lapas.append(fails.parse(lapa))
print(lapas[0]["Nosaukums"]) 
#lapas[0]["Cena"] = lapas[0]["Pašizmaksa"] + (0.31 * lapas[0]["Pašizmaksa"] )


""" lapas_nr = 1
with pandas.ExcelWriter("rezult.xlsx") as fails:
    for lapa in lapas:
        lapa.to_excel(fails, sheet_name= str(lapas_nr), index=False)
        lapas_nr += 1 """