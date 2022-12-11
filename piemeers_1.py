import pandas

excel_fails = "dzivnieki.xls"
#dati = pandas.read_excel(excel_fails)
#print(dati["Suga"].str.len())

# t = "MANS TEKSTS"
# print(t.lower())

print("\n\nvisu uz reizi:")
viss_fails = pandas.ExcelFile(excel_fails)
#print (viss_fails)
lapas = []
for lapa in viss_fails.sheet_names:
    lapas.append(viss_fails.parse(lapa))
print(lapas[0].info())
print(lapas[1])