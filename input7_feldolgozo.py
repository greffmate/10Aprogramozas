import file_fvk as file

sorok=file.beolvasas("input7")
print(sorok)

egysor=sorok[0].split(",")
print(egysor)
szamok=file.strListToIntList(egysor)
print(szamok)