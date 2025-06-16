import pyperclip
import tkinter as tk

def convertir():
    print("Conversion en cours")
    hex_input = champ.get()
    if hex_input == "":
        print("Erreur dans les données")
        resultat_var.set("Erreur : Données invalides")
        return
    try:
        hex_values = hex_input.strip().split()
        dec_values = [int(h, 16) for h in hex_values]
        dec_string = ','.join(f"{d:02d}" for d in dec_values)
        print("Valeurs décimales :", dec_string)
        resultat_var.set(dec_string)
        pyperclip.copy(dec_string)
        print("La chaîne en décimal a été copiée dans le presse-papier.")
        pressepapier.config(text="La chaîne en décimal a été copiée dans le presse-papier.")
    except ValueError:
        print("Erreur dans les données")
        resultat_var.set("Erreur : Données invalides")

def effacer():
    champ.delete(0, 'end')
    resultat_var.set("")
    resultat_affiche.delete(0, 'end')
    pressepapier.config(text="")
    
window = tk.Tk()
window.title("Convertisseur Hex to Dec Brightsign")
window.geometry("500x250")
window.iconbitmap("C:/Users/Rémy Prosperi/OneDrive - Rc Group/Documents/@_MesNotes/PYTHON/convertisseur.ico")

label = tk.Label(window,text="Entrez les valeurs en hex séparées par des espaces :")
label.pack(pady=10)

champ = tk.Entry(window,width = 60)
champ.pack(pady=10)

button_convertir = tk.Button(window, text="Convertir", command=convertir)
button_convertir.pack(pady=10)

resultat_var = tk.StringVar()
resultat_affiche = tk.Entry(window, textvariable=resultat_var, width=60, state="readonly", justify="center", readonlybackground="white")
resultat_affiche.pack(pady=10)

pressepapier= tk.Label(window, text="")
pressepapier.pack(pady=10)

button_effacer = tk.Button(window, text="Effacer", command=effacer)
button_effacer.pack(pady=10)

window.mainloop()


    


