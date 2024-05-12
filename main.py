from tkinter import * 

fenetre = Tk()

fichier = open("data.txt", "a+")  # Ouvrir le fichier en mode ajout (append) ou lecture/Ã©criture (si le fichier n'existe pas, il sera crÃ©Ã©)

imagecookie = PhotoImage(file="cookie.png")

fenetre.geometry("500x500")
cookie = 0  # Initialise le nombre de cookies Ã  0

# Lire le contenu du fichier pour rÃ©cupÃ©rer le nombre de cookies prÃ©cÃ©demment enregistrÃ©
fichier.seek(0)  # Se dÃ©place au dÃ©but du fichier
data = fichier.read()
if data:  # VÃ©rifie si des donnÃ©es ont Ã©tÃ© lues
    cookie = int(data)  # Convertit les donnÃ©es lues en entier

def onclick():
    global cookie
    cookie += 1
    print(cookie)
    counter.config(text='Nombre de cookies : ' + str(cookie))

def quitandsave():
    fichier.seek(0)  # Se dÃ©place au dÃ©but du fichier
    fichier.truncate()  # Efface le contenu du fichier
    fichier.write(str(cookie))  # Ã‰crit le nouveau nombre de cookies dans le fichier
    fenetre.destroy()

menubar = Menu(fenetre)
menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Quitter et sauvegarder", command=quitandsave)
menubar.add_cascade(label="Fichier", menu=menu1)
fenetre.config(menu=menubar)

counter = Label(fenetre, text='Nombre de cookies : ' + str(cookie))
counter.pack()    

bouttoncookie=Button(fenetre, image=imagecookie,command=onclick)
bouttoncookie.pack()

fenetre.mainloop()
fichier.close()