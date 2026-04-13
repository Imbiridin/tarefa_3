letra = input('Digite uma letra para saber se ela é vogal ou consoante: ').lower()

if letra == 'a' or 'e' or 'i' or 'o' or 'u':
    print(f'A letra {letra} é vogal !')
else:
    print(f'A letra {letra} é consoante')