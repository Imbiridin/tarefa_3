print("-" * 50)
turno = input(" Digite de qual turno você é:   "
"('M' para Matutino, 'V' para Vespertino e 'N' para Noturno)" ).lower()
print("-" * 50)

if turno == 'm':
    print("Bom dia!")
elif turno == 'v':
   print("Boa tarde!")
elif turno == "n":
    print("Boa noite!")
else:
    print("Turno Inválido!")
