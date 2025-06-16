import pyperclip

while(True):
    print("Convertisseur hex to dec pour Brightauthor")
    print("==========================================")
    hex_input = input("Entrez les valeurs hexadécimales séparées par des espaces : ")
    hex_values = hex_input.strip().split()
    dec_values = [int(h, 16) for h in hex_values]
    dec_string = ', '.join(str(d) for d in dec_values)
    print("Valeurs décimales :", dec_string)
    pyperclip.copy(dec_string)
    print("La chaîne en décimal a été copiée dans le presse-papier.")
    choix = input("Avez vous d'autres valeurs à convertir ? (o/n) : ")
    if choix == "o":
        continue
    else: break


